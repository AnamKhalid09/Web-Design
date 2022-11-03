# Web-Design

Background
Data becomes more powerful when you share it with others! That’s because people can use your data only if they can access it. So, you’ll use HTML and CSS to create a dashboard featuring the Latitude vs. X analysis of weather.

“”

Before You Begin
Create a new repository for this project called Web-Design-Challenge. Do not add this assignment to an existing repository.

Clone the new repository to your computer.

Inside your local Git repository, add the following:

Three folders named assets, Resources and visualisations.

NOTE
You’ll later add your CSS and image files to the assets folder. You’ll add the CSV file containing the data for your website to the Resources folder. You’ll add the HTML pages that display your visualisations to the visualisations folder.

An index.html file in the main folder.

NOTE
You’ll later edit this file to be the landing page that a user first encounters when reviewing your submission.

Inside the assets folder, two more folders named css and images.

NOTE
You’ll use these folders to store your CSS assets and image assets, respectively.\*

Push the changes from Steps 1–3 to GitHub.

Deploy your index.html file to GitHub Pages.

NOTE
By deploying this empty HTML file to GitHub Pages now, you’ll find that it automatically refreshes as you build your pages. You can then review the updates with each push that you make to GitHub.

Files
Download the following files to help you get started:

Module 11 Challenge files

Instructions
Create a website by using either the visualisations that you created for your Python-APIs Challenge or the weather data and images that are provided for this Challenge. To do so, use the considerations and website requirements that the following subsections describe. Also, ensure that your repository has regular commits and a descriptive README.md file.

NOTE
As you build this dashboard, you'll create a page for each plot and a way to navigate among these pages. These pages should contain the visualisations and the descriptions. You’ll also create two more pages. One will be a landing page that provides a comparison of all the plots. The other will be a page that presents the data used to build the plots.

Considerations
Be aware that you must use Bootstrap. This includes using the Bootstrap navbar component for the header on every page, the Bootstrap grid for responsiveness on the comparison page, and the Bootstrap table component for the data page.

Be aware that you must deploy your website to GitHub Pages, and that as a result, the website must work at a live, publicly accessible URL.

Make sure to use a CSS media query that uses Bootstrap and/or @media for the navigation bar.

Make sure that your website works at all window widths.

Feel free to take some liberties with the visual aspects, but keep the core functionality the same as the instructions describe. (For example, keep the comparison visualisations on the comparison page.)

Website Requirements
The overall requirements for your website are as follows:

NOTE
For reference, review the following Screenshots section.

Your website must consist of seven pages.

At the top of every page, your website must have a navigation bar.

Your website must be deployed to GitHub Pages.

Next, we’ll describe these requirements in detail.

Your website must consist of seven pages as follows:

A landing page that contains the following elements:

An explanation of the project.

A link to each visualisation page. For these, a sidebar should contain a preview image of each visualisation. Clicking an image should take the user to that visualisation.

Four visualisation pages, stored in the visualisations folder, each with the following elements:

A descriptive title and a heading tag.

The visualisation for the selected comparison (latitude vs. max temperature, latitude vs. humidity, latitude vs. cloudiness, or latitude vs. wind speed). The images that these pages display should be stored in the assets/images folder.

A paragraph describing the visualisation and its significance.

A comparisons page that does the following:

Contains all the visualisations on the same page so that people can easily compare them.

Uses a Bootstrap grid for the visualisations. This grid must contain two visualisations across a medium or large screen and one visualisation across an extra-small or small screen.

A data page that displays a responsive table containing the data that the visualisations use, as follows:

The table must be a Bootstrap table component.

HINT
The data must come from either exporting or converting the CSV file to HTML. To do so, try using a tool that you already know: Pandas. Pandas has a to_html method that generates an HTML table from a Pandas DataFrame. To learn more, see pandas.DataFrame.to_htmlLinks to an external site. in the official Pandas documentation.

At the top of every page, your website must have a navigation bar that does the following:

Contains the name of the site on the left side of the navigation bar, allowing users to return to the landing page from any page.

Contains a drop-down menu, named Plots, on the right side of the navigation bar that contains a link to each visualisation page.

Provides two more text links on the right side: Comparisons, which links to the comparisons page, and Data, which links to the data page.

Is responsive (via media queries). Note that the navigation bar must resemble the one in the screenshots in the Navigation Bar section. In particular, notice the background colour change.

Your website must be deployed to GitHub Pages:

As a result, the website must work at a live, publicly accessible URL. Save this URL for your later submission.
Bonus
For extra challenges, try any or all of the following:

Use the same requirements but a different dataset to make it your own.

Use the same requirements, but add a Bootstrap theme to customise your website. To do so, you can use a tool like BootswatchLinks to an external site..

Add extra visualisations.

Use meaningful glyphicons next to the links in the navigation bar.

On every visualisation page that has an active state, add visualisation navigation, as shown in the following images in the Screenshots section.

Screenshots
This section contains screenshots of each page, at various screen widths, that you must create. Keep in mind that these screenshots are intended as a guide. You can meet the requirements without exactly matching your pages to the screenshots.

Landing Page
Small screen landing page

Small screen landing page￼

Comparisons Page
Large screen comparison page

Small screen comparison page

Data Page
Large screen data page

Small screen data page

Visualisation Pages
Large screen example visualisation page

Small screen example visualisation page

Navigation Bar
Large screen navigation bar

Small screen navigation bar

References
OpenWeatherMap.org. (2022). Сurrent weather and forecast. Retrieved from https://openweathermap.org/Links to an external site..
