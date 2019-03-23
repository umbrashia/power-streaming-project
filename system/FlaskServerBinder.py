class FlaskServerBinder:

    localRequest = None
    module = None
    subModule = None
    parm1 = ""
    parm2 = ""

    @staticmethod
    def setData(module=None,
                subModule=None,
                parm1="",
                parm2=""):
        FlaskServerBinder.module=module
        FlaskServerBinder.subModule=subModule
        FlaskServerBinder.parm1=parm1
        FlaskServerBinder.parm2=parm2
