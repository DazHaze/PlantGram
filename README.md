
# Wlecome to Planda!
Planda is a growing community of plant enthusiasts that love to share their house plants. 
Share all the plants you are proud of and talk to people about their plants by interacting on their posts. 
Like the plants you see ? Then like them!

This was created for a project for the Full Stack Development course hosted by [Code Institute](https://codeinstitute.net/ie/5-day-coding-challenge/?utm_term=code%20institute&utm_campaign=CI+-+IRL+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=539453915484&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiAzMGNBhCyARIsANpUkzORRe5o1VJJG9_EwnX2Oxn-ftPjCcE-f8G-M0uOoLartu-8DkXRH5YaAozNEALw_wcB).


![Responsive](https://raw.githubusercontent.com/DazHaze/PlantGram/main/media/responsive.png)
[Planda (Link to external site)](https://plantgram-2022.herokuapp.com/)


## Scope

Due to the timeframe of this project it was important to keep the scope small as to maintain an achievable goal. The website in it's final form was to be fully functional with minimal bugs and a pleasant experience for the user. A list of current goals and future goals was kept by using user stories as 'issues' on github and pairing them with a basic kanban board. Seen in the image below:

![User Stories](https://raw.githubusercontent.com/DazHaze/PlantGram/main/media/user_stories.png)


## Features

### **Design**


While designing Planda it was important to look at existing websites that had solid design principles. The most obvious example was Instagram. While being the social media giant of sharing photos and creating user interactions. Instagram at it's core follows basic design rules.

While designing Planda it was important that it was kept simple and intuitive for the user. Mockups were created using Photoshop for the 'cards' that contain the user posts.

Green was chosen as the main color except from white because of it's associations with plants and orange was chosen as the main accent color as it is a complimentary color to the chosen green. An example of this can be seen in the post card header.

![Card Header](https://raw.githubusercontent.com/DazHaze/PlantGram/main/media/post_header.png)

### **Existing Features**

* Landing Page

![Landing Page](https://raw.githubusercontent.com/DazHaze/PlantGram/main/media/Landing-page.png)

The landing page is kept simple while still bringing in common design elements that are seen throughout the website. The user can either login in or register if they do not have an account. Page is responsive using bootstrap and has been tested on many devices.

![List View](https://raw.githubusercontent.com/DazHaze/PlantGram/main/media/list_view.png)

In the image above the main "timeline" of the website can be seen. This is where the user can view and interact with posts. If the user likes a post in this view, or selects "Leave a comment" then they are taken to a view where only that post is visible and a text inpput to leave a comment is visible. This is called the "Post Detail" view which is seen in the image below.

![Post Detail](https://raw.githubusercontent.com/DazHaze/PlantGram/main/media/post_detail.png)

----


### **Future Features**

* Plants are catagorised based on the users chosen catagories.
* Post funcionality will accept multiple plant images.
* Users can follow other users, showing their posts first on post list view.
* Users can start discussions about plants.

## Testing

  Views were tested through automatic testing using Django. Switching databases was required to get these tests to funtion. The reason for this being a necessity is still not understood.

  Valuable user testing was done through sharing the project with friends and family and having them report bugs in a social media group that was created and also critique design choices and accessibility.

  To publicly share a non-depoloyed website using gitpod:

  1. Use the 'python3 manage.py runserver'
  2. Go to the 'Remote Explorer' tab on the left of screen (monitor icon).
  3. Beside the 8000 port click the open padlock.
  4. Click the globe icon beside that and copy the address in the address bar.
  5. Now share this address. (Only works as long as the server is running in your gitpod window)



## Frameworks Used

* [Django](https://www.djangoproject.com/)

Django was used to create models, views. Link databases and use python as the backend. Django was the backbone of this project.

* [Cloudinary](https://cloudinary.com/documentation/image_video_and_file_upload?utm_source=google&utm_medium=cpc&utm_campaign=Goog_Ent_Srch_PM_NonBrand_ROW&utm_content=591997517453&utm_term=&utm_id=8120040125&gclid=Cj0KCQjw-JyUBhCuARIsANUqQ_IUPR1MKKLwDhv7DBvwHl9XIn1isfAGhTDXyjLtx-6sZuigj8t3TL4aAs3kEALw_wcB)

Cloudinary was used as cloud storage for the images the users uploaded for each post. It also hosts the static files for this website.

* [Github](https://github.com/)

Github was used to create a repository to host the files for this project. It created the ability for version control. Github was also used to create a kanban board for user stories.

* [Techsini](https://techsini.com/)

[Techsini multi device mockup](https://techsini.com/multi-mockup/index.php) was used to create an image of the website being responsive on multiple devices.

* [Bootstrap](https://getbootstrap.com/)

Bootstrap was used to keep the website responsive across all devices to insure a comfortable user experience.




## Deployment
This project was deployed using Heroku. During deployment Heroku had a [security breach](https://blog.heroku.com/github-integration-update) where an attacker gained access to OAuth tokens for heroku - github integration. This meant that this project, while still on Github, was also migrated to Git to be deployed using Heroku. A credit to the Heroku team for showing how to easily do this process while they work on getting the Github integration back up and running. - 20/05/2022


## Credits
* [Code Institute](https://codeinstitute.net/all-access-coding-challenge/?utm_term=code%20institute&utm_campaign=CI+-+IRL+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=539453915484&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiAv_KMBhAzEiwAs-rX1PXOCAky8yjljHzgvSnccpkyUOvNLVGMuzG11t86weTdFdPiTfNHHhoCFuwQAvD_BwE) This project was created for Code Institute's Project 4.

* The code institute slack community!
