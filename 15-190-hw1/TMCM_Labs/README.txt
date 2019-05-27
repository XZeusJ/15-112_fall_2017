
README file for the TMCM_Labs archive                      June 2004
-------------------------------------

This archive contains software and example files for the labs that
are available at http://math.hws.edu/TMCM/java/
You might want to make use of this software while reading the labs
in a Web browser.

The file  TMCM_Labs.jar  contains all the Java software in the form
of a stand-alone application.  When you run this jar file, you will
get a small window with buttons that you can click to run the software
for each of the labs, with the appropriate example files.  Since
you will be running the software outside a Web browser, you will be
able to use the "Save file" and "Load file" capabilities of the software.

The material in this archive can be freely redistributed and used for
non-commercial purposes.

Depending on how Java is installed on your computer, you might be able
to run  TMCM_Labs.jar  simply by double-clicking it.  Alternatively,
you can try entering one of the following commands on the command line.
These commands will work for newer versions of Java:

        java  -jar  TMCM_Labs.jar
        
        java  -cp  TMCM_Labs.jar  tmcm.Labs
        
If you have only the version of Java that came with Internet Explorer,
you can try this command in a command window:

        jview  -cp  TMCM_Labs.jar  tmcm.Labs
        
Finally, if you have a rather old, non-Microsoft version of Java,
the command will be more complicated, since you will have to specify
the location of Java's built-in classes.  For example, if you have
Java version 1.1.8 installed in the directory C:\jdk1.1.8 under windows,
then the command is:

        java  -classpath TMCM_Labs.jar;C:\jdk1.1.8\lib\classes.zip  tmcm.Labs

Under Linux/UNIX, Java 1.1 might be, for example, in the directory
/usr/lib/java, and the command would be

        java  -classpath TMCM_Labs.jar:/usr/lib/java/lib/classes.zip  tmcm.Labs

If you have trouble running the program, consult the Java documentation
to find our how you are supposed to run stand-alone applications writen
in Java.  

----------------------------------------------
David Eck
Department of Mathematics and Computer Science
Hobart and William Smith Colleges
Geneva, NY   14456    USA
Email:  eck@hws.edu
WWW:    http://math.hws.edu/eck/
