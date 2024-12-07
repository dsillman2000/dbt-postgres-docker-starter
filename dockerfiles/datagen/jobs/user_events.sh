PATH="$PATH:/usr/local/bin"
while : 
do
    cd /project
    echo "$(date +'%Y-%m-%d %H:%M:%S') - Installing 'user_events' job"
    poetry -q install
    echo "$(date +'%Y-%m-%d %H:%M:%S') - Starting 'user_events' job"
    poetry -q run datagen user_events
    echo "$(date +'%Y-%m-%d %H:%M:%S') - Done."
    sleep 10
done;
