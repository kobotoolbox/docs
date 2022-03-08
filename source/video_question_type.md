# Video Question Type
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/video_question_type.md" class="reference">15 Feb 2022</a>

The question type "video" prompts a user to record a video as an answer to a
question (e.g. "Please record a video of the head of household saying his full
name"). That video then gets saved along with the form data.

**Advanced**

Including a video as a part of the question is more advanced and can't be done
directly in the KoboToolbox interface. To do this, you need to add a line to
your XML form
([here is an example](https://drive.google.com/file/d/1hntTE1WbAwigcsbOFGgEbO1vEWJPs6uS/view)).

In this example, the question, line 9 is the addition that adds a video to the
label of the question, so that the user sees both the question label ('Sample
video') and the video itself. Note that it references a video file name that
needs to refer to an actual file that is located in a folder 'video' inside your
/sdcard/odk/forms folder, and is called 'sample.3gp'.
