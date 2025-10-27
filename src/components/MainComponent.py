import components.UploadResumeJd as uploadResumeJd
import components.Interview as interview

PAGES = {
  "interview": interview.render,
  "upload": uploadResumeJd.render,
}