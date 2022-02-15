# Video Question Type
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/be4dbc17706d535fe328b67a126df47f57bf573b/source/video_question_type.md" class="reference">25 Jul 2020</a>

The question type "video" prompts a user to record a video as an answer to a question (e.g. "Please record a video of the head of household saying his full name"). That video then gets saved along with the form data. 

**Advanced**

Including a video as a part of the question is more advanced and can't be done directly in the KoboToolbox interface. To do this, you need to add a line to your XML form ([here is an example](https://drive.google.com/file/d/1hntTE1WbAwigcsbOFGgEbO1vEWJPs6uS/view)).  

In this example, the question, line 9 is the addition that adds a video to the label of the question, so that the user sees both the question label ('Sample video') and the video itself. Note that it references a video file name that needs to refer to an actual file that is located in a folder 'video' inside your /sdcard/odk/forms folder, and is called 'sample.3gp'. 
