CREATE TABLE IF NOT EXISTS "incident_api_incident"
        ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "crime_id" integer NOT NULL,
        "original_crime_type_name" text NOT NULL, "report_date" datetime NOT NULL,
        "call_date" datetime NOT NULL, "offense_date" datetime NOT NULL, "call_time" datetime NOT NULL,
        "call_date_time" datetime NOT NULL, "disposition" text NOT NULL, "address" text NOT NULL, "city" text NULL,
        "state" text NOT NULL, "agency_id" integer NOT NULL, "address_type" text NOT NULL, "common_location" text NULL);

CREATE INDEX IF NOT EXISTS "incident_api_incident_report_date_fafaa8af"
            ON "incident_api_incident" ("report_date");