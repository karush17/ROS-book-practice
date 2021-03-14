import rospy
from basics.srv import WordCount, WordCountResponse

def count_words(request):
    return WordCountResponse(len(request.word.split()))

rospy.init_node('service_server')

service = rospy.Service('word_count', WordCount, cont_words)
rospy.spin()
