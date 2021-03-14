rosparam set use_sim_time true
rosrun gmapping slam_gmapping
rosbag play --clock data.bag