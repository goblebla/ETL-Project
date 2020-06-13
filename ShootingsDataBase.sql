DROP TABLE IF EXISTS Shooting
CREATE TABLE Shootings (
    "Name" varchar(100)   NOT NULL,
    "Date" Date   NOT NULL,
    "Death_Cause" varchar(100)   NOT NULL,
    "Armed" varchar(100)   NOT NULL,
    "Age" int   NOT NULL,
	"Gender" varchar(100)   NOT NULL,
    "Race" varchar(100)   NOT NULL,
    "City" varchar(100)   NOT NULL,
    "Mental_illnes" varchar(100)   NOT NULL,
    "Threat_level" varchar(100)   NOT NULL,
    "Fleeing" varchar(100)   NOT NULL,
	"Body_camera" varchar(100)   NOT NULL,
    "Address" varchar(100)   NOT NULL,
    "Zipcode" int   NOT NULL,
    "County" varchar(100)   NOT NULL,
    "Agency" varchar(100)   NOT NULL,
    "Description" varchar(100)   NOT NULL,
	"Disposition_of_death" varchar(100)   NOT NULL,
    "Criminal_charges" varchar(100)   NOT NULL,
    "Alleged_weapon" varchar(100)   NOT NULL,
    CONSTRAINT "Shootings" PRIMARY KEY (
        "ID"
     )
);