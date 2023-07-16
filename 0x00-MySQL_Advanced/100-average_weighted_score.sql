-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DELIMITER $$
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weight_factor FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;
    
    -- Calculate the total weight
    SELECT SUM(weight) INTO total_weight FROM projects;
    
    -- Calculate the weighted score for the user
    SELECT SUM(corrections.score * projects.weight) INTO weighted_score
    FROM corrections
    LEFT JOIN projects ON project_id = projects.id
    WHERE user_id = corrections.user_id;
    
    -- Calculate the weight factor
    SET weight_factor = weighted_score / total_weight;
    
    -- Update the average_weighted_score in the users table
    UPDATE users
    SET average_score = weight_factor
    WHERE id = user_id;
END
$$
DELIMITER ;
