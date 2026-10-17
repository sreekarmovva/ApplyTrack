CREATE TABLE applications(
id SERIAL PRIMARY KEY,
company VARCHAR(100),
role VARCHAR(100),
status VARCHAR(50)
);

INSERT INTO applications (company, role, status)
VALUES ('Google', 'Software Engineer', 'applied');

SELECT* FROM applications;

UPDATE applications
SET status = 'assessment'
WHERE id = 1;

SELECT* FROM applications;

INSERT INTO applications (company, role, status)
VALUES ('TestCompany', 'Test Role', 'applied');

DELETE FROM applications
WHERE company = 'TestCompany';

SELECT * FROM applications;