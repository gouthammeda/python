"""
Author : Prudhvi Akella
"""

print("Inside Biology Module")


class Biology(object):

    @staticmethod
    def morphology():
        print("the study of the forms of things")

    @staticmethod
    def physiology():
        print("the branch of biology that deals with the normal functions of living organisms and their parts.")

    @staticmethod
    def anatomy():
        print("a study of the structure or internal workings of something")


def what_is_biology():
    return "the study of living organisms, divided into many specialized fields that cover their morphology, " \
           "physiology, anatomy, behaviour, origin, and distribution. "
