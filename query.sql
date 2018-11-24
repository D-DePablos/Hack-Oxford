set foreign_key_checks=0;

DROP TABLE IF EXISTS Lecturer;

CREATE TABLE IF NOT EXISTS Lecturer (
	Lecturer_No INT(10),
    First_Name VARCHAR(50),
    Second_Name VARCHAR(50),
    Module_No INT(10),
    FOREIGN KEY (Module_No) REFERENCES Module(Module_No),
    PRIMARY KEY(Lecturer_No)
);

DROP TABLE IF EXISTS Student;

CREATE TABLE IF NOT EXISTS Student (
	Student_No INT(10),
    First_Name VARCHAR(50),
    Second_Name VARCHAR(50),
    PRIMARY KEY(Student_No), 
    Module_No INT(10),
    FOREIGN KEY (Module_No) REFERENCES Module(Module_No)
);

DROP TABLE IF EXISTS Module;

CREATE TABLE IF NOT EXISTS Module (
	Module_No INT(10),
    Module_Name VARCHAR(50),
    Student INT (10),
    TaughtBy INT(10),
    FOREIGN KEY (Student) REFERENCES Student(Student_No),
    FOREIGN KEY (TaughtBy) REFERENCES Lecturer(Lecturer_No),
    PRIMARY KEY(Module_No)
);

DROP TABLE IF EXISTS Questionarie ;

CREATE TABLE IF NOT EXISTS Questionarie (
	Student INT(10),
	Question_No INT(10),
    Question1 VARCHAR(20),
    Question2 VARCHAR(20),
    Question3 VARCHAR(20),
    Question4 VARCHAR(20),
    Question5 VARCHAR(20),
    Question6 VARCHAR(20),
    Question7 VARCHAR(20),
    Question8 VARCHAR(20),
    Question9 VARCHAR(20),
    Question10 VARCHAR(20),
    Question11 VARCHAR(20),
    FOREIGN KEY (Student) REFERENCES Student(Student_No),
    PRIMARY KEY(Question_No)
);

DROP TABLE IF EXISTS Answer;

CREATE TABLE IF NOT EXISTS Answer (
	Student INT(10),
	Answer_No INT(10),
    Answer1 VARCHAR(20),
    Answer2 VARCHAR(20),
    Answer3 VARCHAR(20),
    Answer4 VARCHAR(20),
    Answer5 VARCHAR(20),
    Answer6 VARCHAR(20),
    Answer7 VARCHAR(20),
    Answer8 VARCHAR(20),
    Answer9 VARCHAR(20),
    Answer10 VARCHAR(20),
    Answer11 VARCHAR(20),
    FOREIGN KEY (Student) REFERENCES Student(Student_No),
    PRIMARY KEY(Answer_No)
);