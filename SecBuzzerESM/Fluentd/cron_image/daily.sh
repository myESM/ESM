#Variable setting
createDay="$(date +'%Y-%m-%d' -d'+1 day')"
deleteDay="$(date +'%Y-%m-%d' -d'-365 day')"

#Delete ninety days ago index
curl -X DELETE "localhost:19200/lm-$deleteDay*?pretty"
