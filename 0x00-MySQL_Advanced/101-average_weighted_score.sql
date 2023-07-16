-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE total_weight INT;
	
	-- Calculate the total weight
	SELECT SUM(weight) INTO total_weight FROM projects;
	-- Create temporary table
	CREATE TEMPORARY TABLE weighted_score_table
	SELECT user_id, SUM(corrections.score * projects.weight) / total_weight AS weighted_score
	FROM corrections
	LEFT JOIN projects ON project_id = projects.id
	GROUP BY user_id;
	-- Calculate the weight factor
	-- Update the average_weighted_score in the users table
	UPDATE users
	INNER JOIN weighted_score_table ON users.id = weighted_score_table.user_id
	SET users.average_score = weighted_score_table.weighted_score;
	-- Deleted the temporary table
	DROP TABLE weighted_score_table;
END
$$
DELIMITER ;
