class Servidor(object):
    def __init__(self, listVote):
        self.__listVote = listVote

    def listVoteGet(self):
        return self.__listVote

    def listVoteSet(self, listVote):
        self.__listVote = listVote