import numpy as np
import pandas as pd
import time
from scipy import sparse
from scipy.sparse import csgraph
import networkx as nx

from app.graph import GraphConvolution
from app.utils import *

from keras.models import Model
from keras.layers import Dense, Input, Dropout
from keras.regularizers import l2
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from keras import backend as K

from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from keras import backend as K


class OneModeProjection:


    def __init__(self, nu):
        self.nu = nu

    
    def getOMPSimilarityMatrix(self, dic, ip):
        #OneModeProjection 相似度矩陣：彼此共同連線的比例，雙向矩陣
        similarity_matrix = np.zeros((len(ip), len(ip)))       
        for i in range(0, len(ip)):
            for j in range(0, len(ip)):
                if i == j:
                    continue
                elif float(len(dic[ip[i]] | dic[ip[j]])) == 0:
                    continue
                else:
                    similarity_matrix[i][j] = float(len(dic[ip[i]] & dic[ip[j]])) / float(len(dic[ip[i]] | dic[ip[j]]))

        return similarity_matrix


    def visualize(self, encoded_imgs_test):
        # 畫出三維圖
        plt.figure()
        ax = plt.subplot(projection='3d')
        # ip scan
        imgs_test = encoded_imgs_test[:5].tolist() + encoded_imgs_test[6:].tolist()
        ax.scatter(np.array(imgs_test)[:, 0], np.array(imgs_test)[:, 1], np.array(imgs_test)[:, 2], c='b')
        ax.scatter(encoded_imgs_test[5][0], encoded_imgs_test[5][1], encoded_imgs_test[5][2], c='r', marker='*')
        # # port scan
        # imgs_test = encoded_imgs_test[1:].tolist()
        # ax.scatter(np.array(imgs_test)[:, 0], np.array(imgs_test)[:, 1], np.array(imgs_test)[:, 2], c='b')
        # ax.scatter(encoded_imgs_test[0][0], encoded_imgs_test[0][1], encoded_imgs_test[0][2], c='r', marker='*')

        # plt.show()


    def oneClassSVM(self, encoded_imgs_test, ve_flag):
        
        encoded_imgs_list = encoded_imgs_test.tolist()
        print(encoded_imgs_list, flush=True)
 
        try:
            # clf = OneClassSVM(gamma='auto', nu=self.nu).fit(encoded_imgs_list)
            clf = EllipticEnvelope(contamination=self.nu).fit(np.array(encoded_imgs_list))   
            print('test: ', clf.predict(encoded_imgs_list), flush=True)
        except ValueError:
            print('ValueError')
            print('Automatic retraining')
            ve_flag = True
            time.sleep(5)
            return [], ve_flag
        else:
            ve_flag = False
            return clf.predict(encoded_imgs_list), ve_flag
        
        '''
        c = 0.01
        for _ in range(99):
            clf = OneClassSVM(gamma='auto', nu=c).fit(encoded_imgs_list)
            print('test: ', clf.predict(encoded_imgs_list), round(c, 2))
            c = c + 0.01 

        g = 0.1
        for _ in range(9):
            print()
            print(g)
            c = 0.01
            for _ in range(99):
                clf = OneClassSVM(gamma=g, nu=c).fit(encoded_imgs_list)
                print('test: ', clf.predict(encoded_imgs_list), round(c, 2))
                c = c + 0.01
            g = g + 0.1
        '''


    def run(self, dict_train, dict_test, feature_train, feature_test, ip_list):

        np.random.seed(2)
        K.clear_session()

        train_smatrix = self.getOMPSimilarityMatrix(dict_train, ip_list)
        test_smatrix = self.getOMPSimilarityMatrix(dict_test, ip_list)

        A = sparse.csr_matrix(train_smatrix)
        A_test = sparse.csr_matrix(test_smatrix)

        X = sparse.csr_matrix(feature_train)
        X_test = sparse.csr_matrix(feature_test)

        # GCN + autoencoder
        SYM_NORM = True
        A_ = preprocess_adj(A, SYM_NORM)
        graph = [X, A_]
        support = 1

        A_test_ = preprocess_adj(A_test, SYM_NORM)
        graph_test = [X_test, A_test_]

        G = [Input(shape=(None, None), batch_shape=(None, None), sparse=True)]
        X_in = Input(shape=(X.shape[1],))

        # encoder layers
        # H = Dropout(0.5)(X_in)
        H = GraphConvolution(12, support, activation='relu', kernel_regularizer=l2(5e-4))([X_in]+G)
        # H = Dropout(0.5)(H)
        Y = GraphConvolution(3, support, activation='relu')([H]+G)

        # decoder layers
        # D = Dropout(0.5)(Y)
        D = GraphConvolution(12, support, activation='relu')([Y]+G)
        # D = Dropout(0.5)(D)
        O = GraphConvolution(A.shape[0], support, activation='relu')([D]+G)

        ve_flag = True
        while(ve_flag):

            # compile model
            autoencoder = Model(inputs=[X_in]+G, outputs=O)

            # construct the encoder model for plotting
            encoder = Model(inputs=[X_in]+G, outputs=Y)

            # compile autoencoder
            autoencoder.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.01))

            from keras.callbacks import EarlyStopping
            PATIENCE = 30
            es_callback = EarlyStopping(monitor='loss', patience=PATIENCE)

            # training
            autoencoder.fit(graph, A_, 
                            # sample_weight=train_mask,
                            epochs=500,
                            batch_size=A.shape[0],
                            shuffle=False, callbacks=[es_callback])

            # plotting
            encoded_imgs_test = encoder.predict(graph_test, batch_size=A_test.shape[0])

            # self.visualize(encoded_imgs_test)
            outlier_list, ve_flag = self.oneClassSVM(encoded_imgs_test, ve_flag)

                
        normal_ip = []
        print('suspicious ip: ', flush=True)
        for i in range(len(outlier_list)):
            if outlier_list[i] == -1:
                print(ip_list[i], flush=True)
            else:
                normal_ip.append(ip_list[i])

        return normal_ip

