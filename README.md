# Artefact
Question 1: The JD spider
1. A spider that scraping comment on JD. The pages are set to 10, at a three-second interval
From my preliminary test, the pages could go unlimited, as long as we don't perform too greedy.
（/jd_comments/jd_comment_spider.py）
2. The data is stored in sqlite, which is literally a single file.
3. The Django project read the data in the sqlite database, and display the data as an API.
![](https://github.com/kadakyo/Artefact/blob/master/Restful.png)
4. The basic keyword searching function means users can input the Chinese characters that might contain in the comments.
For instance, if you input "高大上", all records that include the word will emerge.
![](https://github.com/kadakyo/Artefact/blob/master/search.png)

Question 2: Word Count and Median
1. The two folders have been put, which contain the example poems.
2. The run.sh shell script is the main file. As long as we run "chmod 777 run.sh", we can get the results by "/.run.sh"
3. The two Python scripts work as auxiliary scripts.
