-- script that creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is equal to 0
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE SUMMATION FLOAT;
	IF b = 0 THEN
		SET SUMMATION = 0;
	ELSE
		SET SUMMATION = a/b;
	END IF;
	RETURN SUMMATION;
END
$$
DELIMITER ;
