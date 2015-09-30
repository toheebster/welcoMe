__author__ = 'rogermao'
import Service

class Schedule:

    def __init__(self, roster):
        #initialize services
        self.services = []
        self.services.append(
        	#10/2 - 10/4
        	Service("10/2", "Large Group", 3, 3, 6),
        	Service("10/4", "9:30", 3, 3, 0),
        	Service("10/4", "12:30", 2, 2, 0),

        	#revival
        	Service("10/8", "Large Group", 3, 3, 6),
        	Service("10/9", "Large Group", 3, 3, 0),
        	Service("10/10", "Large group", 2, 2, 0),
        	Service("10/11", "9:30", 3,3,0),
        	Service("10/11", "12:30", 2, 2, 0),

        	#10/23 - 10/25
        	Service("10/23", "Large Group", 3, 3, 6),
        	Service("10/25", "9:30", 3, 3, 0),
        	Service("10/25", "12:30", 2, 2, 0),

        	#10/30 - 11/1
        	Service("10/30", "Large Group", 3, 3, 6),
        	Service("11/1", "9:30", 3, 3, 0),
        	Service("10/1", "12:30", 2, 2, 0),

        	#11/6 - 11/8
        	Service("11/6", "Large Group", 3, 3, 6),
        	Service("11/8", "9:30", 3, 3, 0),
        	Service("11/8", "12:30", 2, 2, 0),

        	#11/13 - 11/15  ALL CAMPUS
        	# Service("11/13", "Large Group", 0, 0, 6),
        	Service("11/15", "9:30", 3, 3, 0),
        	Service("11/15", "12:30", 2, 2, 0),


        	#SKIPPED 11/20 - 11/29 BECAUSE OF THXGIVING BREAK
        	#ASK FOR VOLUNTEERS

        	#12/4 - 12/6 - LOCK IN
        	Service("12/4", "Large Group", 3, 3, 6),
        	Service("12/6", "9:30", 3, 3, 0),
        	Service("12/6", "12:30", 2, 2, 0),



        	)


