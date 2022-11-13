import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


class Subscriptions():
    def __init__(self, filename):
        self.devs = []
        try:
            with open(filename, 'r') as fin:
                first_line = fin.readline()[:-1]
                keys_lst = first_line.split('|')
        except IOError as err:
            print(err)
        try:
            with open(filename, 'r') as fin:
                for line in fin.readlines()[1:]:
                    values_lst = line[:-1].split('|')
                    dev_d = dict(zip(keys_lst, values_lst))
                    self.devs.append(dev_d)
        except IOError as err:
            print(err)

    def subscriptions_owned(self):
        subscriptions_d = {"3_owned": 0, "2_owned": 0, "1_owned": 0}
        for user in self.devs:
            phone = user.get("PhoneService")
            internet = user.get("InternetService")
            streamtv = user.get("StreamingTV")
            streammovie = user.get("StreamingMovies")
            if ((phone == "Yes") and (internet != "No")
                    and ((streamtv == "Yes") or (streammovie == "Yes"))):
                subscriptions_d["3_owned"] += 1
            elif ((phone == "Yes") and (internet != "No")
                    and ((streamtv == "No") and (streammovie == "No"))):
                subscriptions_d["2_owned"] += 1
            elif ((phone == "No") and (internet != "No")
                    and ((streamtv == "Yes") or (streammovie == "Yes"))):
                subscriptions_d["2_owned"] += 1
            elif ((phone == "Yes") and (internet == ("No"))):
                subscriptions_d["1_owned"] += 1
            elif ((phone == "No") and (internet != "No")
                    and ((streamtv == "No") and (streammovie == "No"))):
                subscriptions_d["1_owned"] += 1
        return subscriptions_d
