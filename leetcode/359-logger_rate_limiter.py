class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = []
        self.time_stamps = []
   
    def push_message(self, message, time_stamp):
        self.messages.append(message)
        self.time_stamps.append(time_stamp)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if(message not in self.messages):
            self.push_message(message, timestamp)
            return True
        else:
            idx = self.messages.index(message)
            prev_timestamp = self.time_stamps[idx]
            
            if(timestamp-prev_timestamp>=10):
                self.time_stamps[idx] = timestamp
                return True
            
            return False
            
