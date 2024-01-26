DROP DATABASE IF EXISTS `instagram_database`;

CREATE DATABASE IF NOT EXISTS `instagram_database` DEFAULT CHARACTER SET utf8;

USE `instagram_database`;

DROP TABLE IF EXISTS `instagram_database`.`user_activity`;
DROP TABLE IF EXISTS `instagram_database`.`chat_message`;
DROP TABLE IF EXISTS `instagram_database`.`chat_member`;
DROP TABLE IF EXISTS `instagram_database`.`reaction`;
DROP TABLE IF EXISTS `instagram_database`.`comment`;
DROP TABLE IF EXISTS `instagram_database`.`message`;
DROP TABLE IF EXISTS `instagram_database`.`chat`;
DROP TABLE IF EXISTS `instagram_database`.`post`;
DROP TABLE IF EXISTS `instagram_database`.`story`;
DROP TABLE IF EXISTS `instagram_database`.`follower`;
DROP TABLE IF EXISTS `instagram_database`.`user_details`;
DROP TABLE IF EXISTS `instagram_database`.`user`;

CREATE TABLE IF NOT EXISTS `instagram_database`.`user` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(255) UNIQUE NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `password_hash` VARCHAR(255) NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS `instagram_database`.`user_details` (
    `id` INT PRIMARY KEY,
    `full_name` VARCHAR(100),
    `bio` TEXT,
    `profile_picture` VARCHAR(255),
    FOREIGN KEY (`id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`post` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `caption` TEXT,
    `image_url` VARCHAR(255) NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`story` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `story_url` VARCHAR(255) NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`comment` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `post_id` INT,
    `story_id` INT,
    `text` TEXT NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`post_id`) REFERENCES `instagram_database`.`post`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`story_id`) REFERENCES `instagram_database`.`story`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`reaction` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `post_id` INT,
    `story_id` INT,
    `comment_id` INT,
    `type` ENUM('like', 'dislike', 'love', 'haha', 'wow', 'sad', 'angry') NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`post_id`) REFERENCES `instagram_database`.`post`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`story_id`) REFERENCES `instagram_database`.`story`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`comment_id`) REFERENCES `instagram_database`.`comment`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`follower` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT,
    `follower_id` INT,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`follower_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`message` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `sender_id` INT NOT NULL,
    `receiver_id` INT,
    `text` TEXT NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `is_read` BOOLEAN,
    FOREIGN KEY (`sender_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`receiver_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`chat` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `chat_name` VARCHAR(255) NOT NULL,
    `admin_id` INT NOT NULL,
    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`admin_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`chat_member` (
    `chat_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    PRIMARY KEY (chat_id, user_id),
    FOREIGN KEY (`chat_id`) REFERENCES `instagram_database`.`chat`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`chat_message` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `chat_id` INT NOT NULL,
    `message_id` INT NOT NULL,
    FOREIGN KEY (`chat_id`) REFERENCES `instagram_database`.`chat`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`message_id`) REFERENCES `instagram_database`.`message`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE `instagram_database`.`user_activity` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `date_start` TIMESTAMP NOT NULL,
    `date_finish` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `instagram_database`.`user`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;


DELIMITER //
CREATE TRIGGER before_insert_user_activity
BEFORE INSERT ON user_activity
FOR EACH ROW
BEGIN
    IF NEW.user_id NOT IN (SELECT id FROM user) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'User does not exist';
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertUser(
    IN p_username VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password_hash VARCHAR(255)
)
BEGIN
    -- Параметризована вставка нових значень у таблицю користувачів
    INSERT INTO instagram_database.user (username, email, password_hash)
    VALUES (p_username, p_email, p_password_hash);
END //
DELIMITER ;

CALL InsertUser('john_doe', 'john@example.com', 'hashed_password');

DELIMITER //

CREATE PROCEDURE insert_10_posts()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        INSERT INTO `instagram_database`.`post` (user_id, caption, image_url)
        VALUES (1, CONCAT('Caption ', counter), CONCAT('image_url_', counter));

        SET counter = counter + 1;
    END WHILE;
END //

DELIMITER ;

CALL insert_10_posts();

-- DELIMITER $$
-- CREATE FUNCTION calculate_avg_time_diff(table_name VARCHAR(255)) RETURNS DECIMAL(10,2)
-- BEGIN
--     DECLARE avg_diff DECIMAL(10,2);
--     SET @query = CONCAT('SELECT AVG(TIMESTAMPDIFF(SECOND, date_start, date_finish)) 
--                         INTO @avg_diff
--                         FROM ', table_name);
--     PREPARE stmt FROM @query;
--     EXECUTE stmt;
--     DEALLOCATE PREPARE stmt;
--     RETURN @avg_diff;
-- END $$
-- DELIMITER ;
-- SELECT calculate_avg_time_diff('user_activity');
DELIMITER //
CREATE PROCEDURE calculate_avg_time_diff(IN table_name VARCHAR(255), OUT avg_diff DECIMAL(10,2))
BEGIN
    SET @query = CONCAT('SELECT COALESCE(AVG(TIMESTAMPDIFF(SECOND, date_start, date_finish)), 0) 
                        INTO @avg_diff
                        FROM ', table_name);
    
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    SET avg_diff = COALESCE(@avg_diff, 0);
END //
DELIMITER ;

-- CALL calculate_avg_time_diff('user_activity', @result);
-- SELECT @result;

DELIMITER //
CREATE PROCEDURE wrapper_procedure()
BEGIN
    DECLARE avg_result DECIMAL(10,2);

    -- Виклик процедури calculate_avg_time_diff
    CALL calculate_avg_time_diff('user_activity', avg_result);

    -- Вивід результату
    SELECT avg_result AS avg_time_diff;
END //
DELIMITER ;

-- CALL wrapper_procedure();

DELIMITER //

DELIMITER //

CREATE PROCEDURE create_and_copy_tables()
BEGIN
    DECLARE table1_name VARCHAR(255);
    DECLARE table2_name VARCHAR(255);

    -- Генерація унікальних назв таблиць із штампами часу
    SET table1_name = CONCAT('table_', UNIX_TIMESTAMP(), '_1');
    SET table2_name = CONCAT('table_', UNIX_TIMESTAMP(), '_2');

    -- Створення першої таблиці
    SET @create_table1_query = CONCAT(
        'CREATE TABLE IF NOT EXISTS ', table1_name, ' AS SELECT * FROM story;'
    );
    PREPARE stmt1 FROM @create_table1_query;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;

    -- Створення другої таблиці
    SET @create_table2_query = CONCAT(
        'CREATE TABLE IF NOT EXISTS ', table2_name, ' AS SELECT * FROM story;'
    );
    PREPARE stmt2 FROM @create_table2_query;
    EXECUTE stmt2;
    DEALLOCATE PREPARE stmt2;

    -- Копіювання стрічок із батьківської таблиці в одну з додаткових таблиць
    SET @copy_data_query = CONCAT(
        'INSERT INTO ', IF(RAND() > 0.5, table1_name, table2_name), ' SELECT * FROM story;'
    );
    PREPARE stmt3 FROM @copy_data_query;
    EXECUTE stmt3;
    DEALLOCATE PREPARE stmt3;
END //

DELIMITER ;


-- CALL create_and_copy_tables();

INSERT INTO `instagram_database`.`user` (`username`, `email`, `password_hash`, `date`)
VALUES
    ('user1', 'user1@example.com', 'hashed_password1', '1991-01-01 00:00:00'),
    ('user2', 'user2@example.com', 'hashed_password2', '1992-02-02 12:34:56'),
    ('user3', 'user3@example.com', 'hashed_password3', '1993-03-03 23:45:01'),
    ('user4', 'user4@example.com', 'hashed_password4', '1994-04-04 15:30:00'),
    ('user5', 'user5@example.com', 'hashed_password5', '1995-05-05 08:45:22'),
    ('user6', 'user6@example.com', 'hashed_password6', '1996-06-06 18:12:45'),
    ('user7', 'user7@example.com', 'hashed_password7', '1997-07-07 09:30:15'),
    ('user8', 'user8@example.com', 'hashed_password8', '1998-08-08 21:55:00'),
    ('user9', 'user9@example.com', 'hashed_password9', '1999-09-09 03:20:30'),
    ('user10', 'user10@example.com', 'hashed_password10', '2000-10-10 14:10:05'),
    ('user11', 'user11@example.com', 'hashed_password11', '2001-11-11 04:40:12'),
    ('user12', 'user12@example.com', 'hashed_password12', '2002-12-12 16:25:33'),
    ('user13', 'user13@example.com', 'hashed_password13', '2003-03-14 10:11:22'),
    ('user14', 'user14@example.com', 'hashed_password14', '2004-06-18 05:30:45'),
    ('user15', 'user15@example.com', 'hashed_password15', '2005-09-22 19:48:59');

INSERT INTO `instagram_database`.`user_details` (`id`, `full_name`, `bio`, `profile_picture`)
VALUES
    (1, 'John Doe', 'A passionate Instagram user', 'profile_pic1.jpg'),
    (2, 'Jane Smith', 'Exploring the world through photos', 'profile_pic2.jpg'),
    (3, 'Alice Johnson', 'Photography enthusiast', 'profile_pic3.jpg'),
    (4, 'Bob Anderson', 'Traveler and storyteller', 'profile_pic4.jpg'),
    (5, 'Eva Martinez', 'Nature lover and artist', 'profile_pic5.jpg'),
    (6, 'Chris Wilson', 'Adventurer and foodie', 'profile_pic6.jpg'),
    (7, 'Sophie Brown', 'Fitness freak and health advocate', 'profile_pic7.jpg'),
    (8, 'Mike Taylor', 'Tech geek and gamer', 'profile_pic8.jpg'),
    (9, 'Olivia White', 'Bookworm and writer', 'profile_pic9.jpg'),
    (10, 'Daniel Lee', 'Musician and dreamer', 'profile_pic10.jpg'),
    (11, 'Emily Turner', 'Fashionista and trendsetter', 'profile_pic11.jpg'),
    (12, 'Alex Clark', 'Science nerd and researcher', 'profile_pic12.jpg'),
    (13, 'Grace Walker', 'Animal lover and volunteer', 'profile_pic13.jpg'),
    (14, 'Ryan Moore', 'Business professional and entrepreneur', 'profile_pic14.jpg'),
    (15, 'Lily Green', 'Artist and free spirit', 'profile_pic15.jpg');

INSERT INTO `instagram_database`.`post` (`user_id`, `caption`, `image_url`, `date`)
VALUES
    (1, 'Beautiful sunset view', 'sunset_image1.jpg', '2022-01-01 12:34:56'),
    (2, 'Exploring new places!', 'travel_image2.jpg', '2022-02-02 14:45:00'),
    (3, 'City lights at night', 'cityscape_image3.jpg', '2022-03-03 18:20:15'),
    (4, 'Delicious homemade meal', 'food_image4.jpg', '2022-04-04 20:30:30'),
    (5, 'Hiking in the mountains', 'hiking_image5.jpg', '2022-05-05 08:45:22'),
    (6, 'Artistic photography', 'art_image6.jpg', '2022-06-06 11:12:45'),
    (7, 'Morning workout routine', 'fitness_image7.jpg', '2022-07-07 09:30:15'),
    (8, 'Gaming night with friends', 'gaming_image8.jpg', '2022-08-08 21:55:00'),
    (9, 'Lost in a good book', 'reading_image9.jpg', '2022-09-09 03:20:30'),
    (10, 'Jamming session', 'music_image10.jpg', '2022-10-10 14:10:05'),
    (11, 'Fashion forward', 'fashion_image11.jpg', '2022-11-11 04:40:12'),
    (12, 'Latest tech gadgets', 'tech_image12.jpg', '2022-12-12 16:25:33'),
    (13, 'Helping at the animal shelter', 'volunteer_image13.jpg', '2023-02-14 10:11:22'),
    (14, 'Business success', 'business_image14.jpg', '2023-06-18 05:30:45'),
    (15, 'Abstract artwork', 'art_image15.jpg', '2023-09-22 19:48:59'),
    (1, 'Chasing waterfalls', 'nature_image16.jpg', '2023-11-01 12:34:56'),
    (2, 'Cooking experiment', 'cooking_image17.jpg', '2023-11-02 14:45:00'),
    (3, 'Sunrise meditation', 'meditation_image18.jpg', '2023-11-03 18:20:15'),
    (4, 'Vintage vibes', 'vintage_image19.jpg', '2023-11-04 20:30:30'),
    (5, 'Winter wonderland', 'winter_image20.jpg', '2023-11-05 08:45:22'),
    (6, 'Sunny beach day', 'beach_image21.jpg', '2023-11-06 11:12:45'),
    (7, 'Yoga in the park', 'yoga_image22.jpg', '2023-11-07 09:30:15'),
    (8, 'Late-night coding', 'coding_image23.jpg', '2023-11-08 21:55:00'),
    (9, 'Traveling the world', 'travel_image24.jpg', '2023-11-09 03:20:30'),
    (10, 'Concert vibes', 'concert_image25.jpg', '2023-11-10 14:10:05');

INSERT INTO `instagram_database`.`story` (`user_id`, `story_url`, `date`)
VALUES
    (1, 'story1.mp4', '2022-01-01 12:34:56'),
    (2, 'story2.jpg', '2022-02-02 14:45:00'),
    (3, 'story3.mp4', '2022-03-03 18:20:15'),
    (4, 'story4.jpg', '2022-04-04 20:30:30'),
    (5, 'story5.mp4', '2022-05-05 08:45:22'),
    (6, 'story6.jpg', '2022-06-06 11:12:45'),
    (7, 'story7.mp4', '2022-07-07 09:30:15'),
    (8, 'story8.jpg', '2022-08-08 21:55:00'),
    (9, 'story9.mp4', '2022-09-09 03:20:30'),
    (10, 'story10.jpg', '2022-10-10 14:10:05'),
    (11, 'story11.mp4', '2022-11-11 04:40:12'),
    (12, 'story12.jpg', '2022-12-12 16:25:33'),
    (13, 'story13.mp4', '2023-02-14 10:11:22'),
    (14, 'story14.jpg', '2023-06-18 05:30:45'),
    (15, 'story15.mp4', '2023-09-22 19:48:59'),
    (1, 'story16.jpg', '2023-11-01 12:34:56'),
    (2, 'story17.mp4', '2023-11-02 14:45:00'),
    (3, 'story18.jpg', '2023-11-03 18:20:15'),
    (4, 'story19.mp4', '2023-11-04 20:30:30'),
    (5, 'story20.jpg', '2023-11-05 08:45:22');

INSERT INTO `instagram_database`.`comment` (`user_id`, `post_id`, `story_id`, `text`, `date`)
VALUES
    (1, 1, NULL, 'Great shot!', '2022-01-01 12:34:56'),
    (2, 2, NULL, 'Amazing travel experience!', '2022-02-02 14:45:00'),
    (3, 3, NULL, 'Love the city lights!', '2022-03-03 18:20:15'),
    (4, 4, NULL, 'Delicious looking meal!', '2022-04-04 20:30:30'),
    (5, 5, NULL, 'Incredible view!', '2022-05-05 08:45:22'),
    (6, 6, NULL, 'Beautifully captured!', '2022-06-06 11:12:45'),
    (7, 7, NULL, 'Your workout routine is inspiring!', '2022-07-07 09:30:15'),
    (8, 8, NULL, 'Gaming night goals!', '2022-08-08 21:55:00'),
    (9, 9, NULL, 'What book is that?', '2022-09-09 03:20:30'),
    (10, 10, NULL, 'Jamming session looks fun!', '2022-10-10 14:10:05'),
    (11, 11, NULL, 'Fashion on point!', '2022-11-11 04:40:12'),
    (12, 12, NULL, 'Latest tech gadgets are awesome!', '2022-12-12 16:25:33'),
    (13, 13, NULL, 'Such a heartwarming volunteer work!', '2023-02-14 10:11:22'),
    (14, 14, NULL, 'Impressive business success!', '2023-06-18 05:30:45'),
    (15, 15, NULL, 'Love the abstract art!', '2023-09-22 19:48:59'),
    (1, NULL, 1, 'Beautiful nature shot!', '2023-11-01 12:34:56'),
    (2, NULL, 2, 'Cooking skills on point!', '2023-11-02 14:45:00'),
    (3, NULL, 3, 'Peaceful meditation!', '2023-11-03 18:20:15'),
    (4, NULL, 4, 'Vintage vibes are my favorite!', '2023-11-04 20:30:30'),
    (5, NULL, 5, 'Winter wonderland indeed!', '2023-11-05 08:45:22'),
    (6, NULL, 6, 'Wishing I was at the beach!', '2023-11-06 11:12:45'),
    (7, NULL, 7, 'Yoga goals!', '2023-11-07 09:30:15'),
    (8, NULL, 8, 'Late-night coding session!', '2023-11-08 21:55:00'),
    (9, NULL, 9, 'Amazing travel photos!', '2023-11-09 03:20:30'),
    (10, NULL, 10, 'Concert vibes are the best!', '2023-11-10 14:10:05'),
    (11, NULL, 11, 'Stylish outfit!', '2023-11-11 04:40:12'),
    (12, NULL, 12, 'Fascinating tech discoveries!', '2023-11-12 16:25:33'),
    (13, NULL, 13, 'Supporting animals is wonderful!', '2023-11-13 10:11:22'),
    (14, NULL, 14, 'Congratulations on your business!', '2023-11-14 05:30:45'),
    (15, NULL, 15, 'Your art is so unique!', '2023-11-15 19:48:59'),
    (1, 1, NULL, 'Another breathtaking nature shot!', '2023-11-16 12:34:56'),
    (2, 2, NULL, 'How did you cook that?', '2023-11-17 14:45:00'),
    (3, 3, NULL, 'Meditation goals!', '2023-11-18 18:20:15'),
    (4, 4, NULL, 'Vintage vibes never get old!', '2023-11-19 20:30:30'),
    (5, 5, NULL, 'Winter wonderland part 2!', '2023-11-20 08:45:22'),
    (6, 6, NULL, 'Wishing for a beach day too!', '2023-11-21 11:12:45'),
    (7, 7, NULL, 'Yoga is essential!', '2023-11-22 09:30:15'),
    (8, 8, NULL, 'Code, sleep, repeat!', '2023-11-23 21:55:00'),
    (9, 9, NULL, 'More travel adventures, please!', '2023-11-24 03:20:30'),
    (10, 10, NULL, 'Best concert ever!', '2023-11-25 14:10:05'),
    (11, NULL, 11, 'Fashion icon!', '2023-11-26 04:40:12'),
    (12, NULL, 12, 'The future is tech!', '2023-11-27 16:25:33'),
    (13, NULL, 13, 'Adopt, dont shop!', '2023-11-28 10:11:22'),
    (14, NULL, 14, 'New business milestones!', '2023-11-29 05:30:45'),
    (15, NULL, 15, 'Artistic brilliance!', '2023-11-30 19:48:59'),
    (1, 2, NULL, 'This is even better than the last one!', '2023-12-01 12:34:56'),
    (2, 3, NULL, 'Looks delicious! Can you share the recipe?', '2023-12-02 14:45:00'),
    (3, 4, NULL, 'Meditation is key to a peaceful life.', '2023-12-03 18:20:15'),
    (4, 5, NULL, 'Vintage vibes are my aesthetic.', '2023-12-04 20:30:30'),
    (5, 6, NULL, 'Winter wonderland magic!', '2023-12-05 08:45:22'),
    (6, 7, NULL, 'Wishing I was on that beach right now.', '2023-12-06 11:12:45'),
    (7, 8, NULL, 'Yoga is the best way to start the day.', '2023-12-07 09:30:15'),
    (8, 9, NULL, 'Late-night coding sessions are the most productive!', '2023-12-08 21:55:00'),
    (9, 10, NULL, 'Traveling is my passion!', '2023-12-09 03:20:30'),
    (10, 11, NULL, 'Concert vibes are unmatched.', '2023-12-10 14:10:05'),
    (11, NULL, 12, 'Fashion goals!', '2023-12-11 04:40:12'),
    (12, NULL, 13, 'Tech innovations are changing the world.', '2023-12-12 16:25:33'),
    (13, NULL, 14, 'Supporting animal causes is close to my heart.', '2023-12-13 10:11:22'),
    (14, NULL, 15, 'Congratulations on the business achievements!', '2023-12-14 05:30:45'),
    (15, NULL, 1, 'Your art speaks volumes!', '2023-12-15 19:48:59'),
    (1, 3, NULL, 'Absolutely stunning!', '2023-12-16 12:34:56'),
    (2, 4, NULL, 'What camera did you use for this?', '2023-12-17 14:45:00'),
    (3, 5, NULL, 'City lights always fascinate me.', '2023-12-18 18:20:15'),
    (4, 6, NULL, 'Food is an art form.', '2023-12-19 20:30:30'),
    (5, 7, NULL, 'Impressive workout routine!', '2023-12-20 08:45:22'),
    (6, 8, NULL, 'Gaming night looks like a blast!', '2023-12-21 11:12:45'),
    (7, 9, NULL, 'Yoga in nature is the best.', '2023-12-22 09:30:15'),
    (8, 10, NULL, 'Coding is my therapy.', '2023-12-23 21:55:00'),
    (9, 11, NULL, 'Book recommendations, please!', '2023-12-24 03:20:30'),
    (10, 12, NULL, 'Jamming session goals!', '2023-12-25 14:10:05');

INSERT INTO `instagram_database`.`reaction` (`user_id`, `post_id`, `story_id`, `comment_id`, `type`, `date`)
VALUES
    (1, 1, NULL, NULL, 'like', '2022-01-01 12:34:56'),
    (2, 2, NULL, NULL, 'love', '2022-02-02 14:45:00'),
    (3, 3, NULL, NULL, 'haha', '2022-03-03 18:20:15'),
    (4, 4, NULL, NULL, 'wow', '2022-04-04 20:30:30'),
    (5, 5, NULL, NULL, 'sad', '2022-05-05 08:45:22'),
    (6, 6, NULL, NULL, 'angry', '2022-06-06 11:12:45'),
    (7, 7, NULL, NULL, 'like', '2022-07-07 09:30:15'),
    (8, 8, NULL, NULL, 'love', '2022-08-08 21:55:00'),
    (9, 9, NULL, NULL, 'haha', '2022-09-09 03:20:30'),
    (10, 10, NULL, NULL, 'wow', '2022-10-10 14:10:05'),
    (11, 11, NULL, NULL, 'sad', '2022-11-11 04:40:12'),
    (12, 12, NULL, NULL, 'angry', '2022-12-12 16:25:33'),
    (13, NULL, 13, NULL, 'like', '2023-02-14 10:11:22'),
    (14, NULL, 14, NULL, 'love', '2023-06-18 05:30:45'),
    (15, NULL, 15, NULL, 'haha', '2023-09-22 19:48:59'),
    (1, 16, NULL, NULL, 'wow', '2023-11-01 12:34:56'),
    (2, 17, NULL, NULL, 'sad', '2023-11-02 14:45:00'),
    (3, 18, NULL, NULL, 'angry', '2023-11-03 18:20:15'),
    (4, 19, NULL, NULL, 'like', '2023-11-04 20:30:30'),
    (5, 20, NULL, NULL, 'love', '2023-11-05 08:45:22'),
    (6, 21, NULL, NULL, 'haha', '2023-11-06 11:12:45'),
    (7, 22, NULL, NULL, 'wow', '2023-11-07 09:30:15'),
    (8, 23, NULL, NULL, 'sad', '2023-11-08 21:55:00'),
    (9, 24, NULL, NULL, 'angry', '2023-11-09 03:20:30'),
    (10, 25, NULL, NULL, 'like', '2023-11-10 14:10:05'),
    (11, NULL, 1, NULL, 'love', '2023-11-11 04:40:12'),
    (12, NULL, 2, NULL, 'haha', '2023-11-12 16:25:33'),
    (13, NULL, 3, NULL, 'wow', '2023-11-13 10:11:22'),
    (14, NULL, 4, NULL, 'sad', '2023-11-14 05:30:45'),
    (15, NULL, 5, NULL, 'angry', '2023-11-15 19:48:59'),
    (1, NULL, 6, NULL, 'like', '2023-11-16 12:34:56'),
    (2, NULL, 7, NULL, 'love', '2023-11-17 14:45:00'),
    (3, NULL, 8, NULL, 'haha', '2023-11-18 18:20:15'),
    (4, NULL, 9, NULL, 'wow', '2023-11-19 20:30:30'),
    (5, NULL, 10, NULL, 'sad', '2023-11-20 08:45:22'),
    (6, NULL, 11, NULL, 'angry', '2023-11-21 11:12:45'),
    (7, NULL, 12, NULL, 'like', '2023-11-22 09:30:15'),
    (8, NULL, 13, NULL, 'love', '2023-11-23 21:55:00'),
    (9, NULL, 14, NULL, 'haha', '2023-11-24 03:20:30'),
    (10, NULL, 15, NULL, 'wow', '2023-11-25 14:10:05'),
    (11, NULL, 16, NULL, 'sad', '2023-11-26 04:40:12'),
    (12, NULL, 18, NULL, 'angry', '2023-11-27 16:25:33'),
    (13, NULL, 19, NULL, 'like', '2023-11-28 10:11:22'),
    (14, NULL, 20, NULL, 'love', '2023-11-29 05:30:45'),
    (15, NULL, NULL, 1, 'haha', '2023-11-30 19:48:59'),
    (1, NULL, NULL, 2, 'like', '2023-12-01 12:34:56'),
    (2, NULL, NULL, 3, 'love', '2023-12-02 14:45:00'),
    (3, NULL, NULL, 4, 'haha', '2023-12-03 18:20:15'),
    (4, NULL, NULL, 5, 'wow', '2023-12-04 20:30:30'),
    (5, NULL, NULL, 6, 'sad', '2023-12-05 08:45:22'),
    (6, NULL, NULL, 7, 'angry', '2023-12-06 11:12:45'),
    (7, NULL, NULL, 8, 'like', '2023-12-07 09:30:15'),
    (8, NULL, NULL, 9, 'love', '2023-12-08 21:55:00'),
    (9, NULL, NULL, 10, 'haha', '2023-12-09 03:20:30'),
    (10, NULL, NULL, 11, 'wow', '2023-12-10 14:10:05'),
    (11, NULL, NULL, 12, 'sad', '2023-12-11 04:40:12'),
    (12, NULL, NULL, 13, 'angry', '2023-12-12 16:25:33'),
    (13, NULL, NULL, 14, 'like', '2023-12-13 10:11:22'),
    (14, NULL, NULL, 15, 'love', '2023-12-14 05:30:45'),
    (15, NULL, NULL, 16, 'haha', '2023-12-15 19:48:59'),
    (1, NULL, NULL, 17, 'wow', '2023-12-16 12:34:56'),
    (2, NULL, NULL, 18, 'sad', '2023-12-17 14:45:00'),
    (3, NULL, NULL, 19, 'angry', '2023-12-18 18:20:15'),
    (4, NULL, NULL, 20, 'like', '2023-12-19 20:30:30'),
    (5, NULL, NULL, 21, 'love', '2023-12-20 08:45:22'),
    (6, NULL, NULL, 22, 'haha', '2023-12-21 11:12:45'),
    (7, NULL, NULL, 23, 'wow', '2023-12-22 09:30:15'),
    (8, NULL, NULL, 24, 'sad', '2023-12-23 21:55:00'),
    (9, NULL, NULL, 25, 'angry', '2023-12-24 03:20:30'),
    (10, NULL, NULL, 26, 'like', '2023-12-25 14:10:05'),
    (11, NULL, NULL, 27, 'love', '2023-12-26 04:40:12'),
    (12, NULL, NULL, 28, 'haha', '2023-12-27 16:25:33'),
    (13, NULL, NULL, 29, 'wow', '2023-12-28 10:11:22'),
    (14, NULL, NULL, 30, 'sad', '2023-12-29 05:30:45'),
    (15, NULL, NULL, 31, 'angry', '2023-12-30 19:48:59'),
    (1, NULL, NULL, 32, 'like', '2024-01-01 12:34:56'),
    (2, NULL, NULL, 33, 'love', '2024-01-02 14:45:00'),
    (3, NULL, NULL, 34, 'haha', '2024-01-03 18:20:15'),
    (4, NULL, NULL, 35, 'wow', '2024-01-04 20:30:30'),
    (5, NULL, NULL, 36, 'sad', '2024-01-05 08:45:22'),
    (6, NULL, NULL, 37, 'angry', '2024-01-06 11:12:45'),
    (7, NULL, NULL, 38, 'like', '2024-01-07 09:30:15'),
    (8, NULL, NULL, 39, 'love', '2024-01-08 21:55:00'),
    (9, NULL, NULL, 40, 'haha', '2024-01-09 03:20:30'),
    (10, NULL, NULL, 41, 'wow', '2024-01-10 14:10:05'),
    (11, NULL, NULL, 42, 'sad', '2024-01-11 04:40:12'),
    (12, NULL, NULL, 43, 'angry', '2024-01-12 16:25:33'),
    (13, NULL, NULL, 44, 'like', '2024-01-13 10:11:22'),
    (14, NULL, NULL, 45, 'love', '2024-01-14 05:30:45'),
    (15, NULL, NULL, 46, 'haha', '2024-01-15 19:48:59'),
    (1, NULL, NULL, 47, 'wow', '2024-01-16 12:34:56'),
    (2, NULL, NULL, 48, 'sad', '2024-01-17 14:45:00'),
    (3, NULL, NULL, 49, 'angry', '2024-01-18 18:20:15'),
    (4, NULL, NULL, 50, 'like', '2024-01-19 20:30:30'),
    (5, NULL, NULL, 51, 'love', '2024-01-20 08:45:22'),
    (6, NULL, NULL, 52, 'haha', '2024-01-21 11:12:45'),
    (7, NULL, NULL, 53, 'wow', '2024-01-22 09:30:15'),
    (8, NULL, NULL, 54, 'sad', '2024-01-23 21:55:00'),
    (9, NULL, NULL, 55, 'angry', '2024-01-24 03:20:30'),
    (10, NULL, NULL, 56, 'like', '2024-01-25 14:10:05'),
    (11, NULL, NULL, 57, 'sad', '2024-01-11 04:40:12'),
    (12, NULL, NULL, 58, 'angry', '2024-01-12 16:25:33'),
    (13, NULL, NULL, 59, 'like', '2024-01-13 10:11:22'),
    (14, NULL, NULL, 60, 'love', '2024-01-14 05:30:45'),
    (15, NULL, NULL, 61, 'haha', '2024-01-15 19:48:59');

INSERT INTO `instagram_database`.`follower` (`user_id`, `follower_id`, `date`)
VALUES
    (1, 2, '2022-01-01 12:34:56'),
    (1, 3, '2022-01-02 14:45:00'),
    (1, 4, '2022-01-03 18:20:15'),
    (2, 3, '2022-01-04 20:30:30'),
    (2, 4, '2022-01-05 08:45:22'),
    (2, 5, '2022-01-06 11:12:45'),
    (3, 4, '2022-01-07 09:30:15'),
    (3, 5, '2022-01-08 21:55:00'),
    (3, 6, '2022-01-09 03:20:30'),
    (4, 5, '2022-01-10 14:10:05'),
    (4, 6, '2022-01-11 04:40:12'),
    (4, 7, '2022-01-12 16:25:33'),
    (5, 6, '2022-01-13 10:11:22'),
    (5, 7, '2022-01-14 05:30:45'),
    (5, 8, '2022-01-15 19:48:59'),
    (6, 7, '2022-01-16 12:34:56'),
    (6, 8, '2022-01-17 14:45:00'),
    (6, 9, '2022-01-18 18:20:15'),
    (7, 8, '2022-01-19 20:30:30'),
    (7, 9, '2022-01-20 08:45:22'),
    (7, 10, '2022-01-21 11:12:45'),
    (8, 9, '2022-01-22 09:30:15'),
    (8, 10, '2022-01-23 21:55:00'),
    (8, 11, '2022-01-24 03:20:30'),
    (9, 10, '2022-01-25 14:10:05'),
    (9, 11, '2022-01-26 04:40:12'),
    (9, 12, '2022-01-27 16:25:33'),
    (10, 11, '2022-01-28 10:11:22'),
    (10, 12, '2022-01-29 05:30:45'),
    (10, 13, '2022-01-30 19:48:59'),
    (11, 12, '2022-01-31 12:34:56'),
    (11, 13, '2022-02-01 14:45:00'),
    (11, 14, '2022-02-02 18:20:15'),
    (12, 13, '2022-02-03 20:30:30'),
    (12, 14, '2022-02-04 08:45:22'),
    (12, 15, '2022-02-05 11:12:45');


INSERT INTO `instagram_database`.`message` (`sender_id`, `receiver_id`, `text`, `is_read`, `date`)
VALUES
    (1, 2, 'Hello, how are you?', true, '2022-01-01 12:34:56'),
    (2, 1, 'Hi! Im good, thanks.', false, '2022-01-02 14:45:00'),
    (3, 1, 'Hey there!', true, '2022-01-03 18:20:15'),
    (1, 4, 'Whats up?', false, '2022-01-04 20:30:30'),
    (4, 1, 'Not much, just chilling.', true, '2022-01-05 08:45:22'),
    (2, 3, 'Hows your day going?', false, '2022-01-06 11:12:45'),
    (3, 2, 'Its been good! How about yours?', true, '2022-01-07 09:30:15'),
    (4, 2, 'Hi, long time no talk!', false, '2022-01-08 21:55:00'),
    (2, 5, 'Yeah, its been a while. How have you been?', true, '2022-01-09 03:20:30'),
    (5, 2, 'Ive been great! Thanks for asking.', false, '2022-01-10 14:10:05'),
    (3, 4, 'What are you up to this weekend?', true, '2022-01-11 04:40:12'),
    (4, 3, 'I have some plans with friends. How about you?', false, '2022-01-12 16:25:33'),
    (5, 4, 'Hey! Lets catch up soon.', true, '2022-01-13 10:11:22'),
    (4, 5, 'Sure thing! Im looking forward to it.', false, '2022-01-14 05:30:45'),
    (1, 3, 'Happy birthday!', true, '2022-01-15 19:48:59');

INSERT INTO `instagram_database`.`chat` (`chat_name`, `admin_id`, `date`)
VALUES
    ('Friends Chat', 1, '2022-01-01 12:34:56'),
    ('Work Team', 2, '2022-01-02 14:45:00'),
    ('Family Group', 3, '2022-01-03 18:20:15'),
    ('Study Buddies', 4, '2022-01-04 20:30:30'),
    ('Gaming Squad', 5, '2022-01-05 08:45:22'),
    ('Travel Enthusiasts', 1, '2022-01-06 11:12:45'),
    ('Book Club', 2, '2022-01-07 09:30:15'),
    ('Fitness Freaks', 3, '2022-01-08 21:55:00'),
    ('Tech Talk', 4, '2022-01-09 03:20:30'),
    ('Movie Buffs', 5, '2022-01-10 14:10:05'),
    ('Foodies Corner', 1, '2022-01-11 04:40:12'),
    ('Art Lovers', 2, '2022-01-12 16:25:33'),
    ('Music Maniacs', 3, '2022-01-13 10:11:22'),
    ('Pet Owners', 4, '2022-01-14 05:30:45'),
    ('Techies Hangout', 5, '2022-01-15 19:48:59');

INSERT INTO `instagram_database`.`chat_member` (`chat_id`, `user_id`)
VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (2, 3),
    (3, 3),
    (3, 4),
    (4, 4),
    (4, 5),
    (5, 5),
    (5, 1),
    (6, 1),
    (6, 3),
    (7, 2),
    (7, 4),
    (8, 3),
    (8, 5),
    (9, 1),
    (9, 4),
    (10, 2),
    (10, 5),
    (11, 1),
    (11, 3),
    (12, 2),
    (12, 4),
    (13, 3),
    (13, 5),
    (14, 1),
    (14, 4),
    (15, 2),
    (15, 5);

INSERT INTO `instagram_database`.`chat_message` (`chat_id`, `message_id`)
VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (3, 6),
    (4, 7),
    (4, 8),
    (5, 9),
    (5, 10),
    (6, 11),
    (6, 12),
    (7, 13),
    (7, 14),
    (8, 15);

INSERT INTO `instagram_database`.`user_activity` (`user_id`, `date_start`, `date_finish`)
VALUES
    (1, '2024-01-27 12:00:00', '2024-01-27 13:00:00'),
    (2, '2024-01-27 14:30:00', '2024-01-27 16:00:00'),
    (3, '2024-01-27 18:45:00', '2024-01-27 19:30:00'),
    (4, '2024-01-27 20:15:00', '2024-01-27 21:00:00'),
    (5, '2024-01-27 22:30:00', '2024-01-27 23:45:00');


CREATE UNIQUE INDEX `idx_username` ON `instagram_database`.`user`(`username`);
CREATE UNIQUE INDEX `idx_email` ON `instagram_database`.`user`(`email`);
CREATE INDEX `idx_post_username` ON `instagram_database`.`post`(`user_id`);
CREATE INDEX `idx_message_username` ON `instagram_database`.`message`(`sender_id`);
CREATE INDEX `idx_post_date` ON `instagram_database`.`post`(`date`);

