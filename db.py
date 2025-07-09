
__conn = None
def get_sql_connection():       
    global __conn      
    if __conn is None:                                                     
        DRIVER_NAME = 'SQL SERVER'
        SERVER_NAME = 'DESKTOP-780T5DC'
        DATABASE_NAME = 'EmployeeDetails'

        connection_string = f"""
            DRIVER={DRIVER_NAME}; SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};
            Trust_connection= yes;
        """
        __conn = connection_string
    return __conn


