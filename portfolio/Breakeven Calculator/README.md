# Breakeven Analysis Calculator
#### Video Demo:  <https://youtu.be/51SQidOZOPw>
#### Description:


The Breakeven Analysis Calculator is a web application built with Python and Flask. The calculator allows the user to calculate the breakeven point of a product in unit sales. It also uses html and css for style and layout. The project is implemented for the sole purpose of the CS50 course provided by HarvardX and uniquely developed for that purpose.

The user needs to enter the necessary information below:
- Fixed Costs (or set up up front costs)
- Cost per Item (production cost)
- Shipping Cost if any (if there are any shipping costs, they can be entered here or the user can put 0)
- Other Costs if any (if there are other costs that the calculator does not have a specified field for)
- Sales Price (price at which the product is sold)

If any of the fields is not filled, the user will be re-prompted to enter the information again. If the user doesn't have shipping or other costs, they can put 0. The layout and style of the page is kept very simple to make sure it's user friendly and to the point. Once all input are competed, the user can then press the calculate button at the bottom of the calculator see the results. The number of units that the user should sell to breakeven is shown below the button with a brief explanation as well. If the price of the item is below 0, the user will be shown an error message in red to let them know that their price shouldn't be less than 0 as they cannot breakeven in this way.

Bellow are the descriptions of all the files in the project.




**index.html**

This file includes the basic html elements of the page including the form and all the text, headings, etc. It also handles where to show the results of the calculation when the user inputs all the data and hits calculate button. The file also includes arranging the error messages under each section. The last function is the submit button that the user can press to get the result of the calculation. At the end of the page, the result of the calculation will be shown that is rendered from application.py.

**layout.html**

This includes the template to be used in any html filed and avoid repeating the common elements in every file. It holds the basic html layout for the page and it also includes the background style for the page including the background photo link. The file would be useful for scaling the page and adding other pages that use the same layout without repeating the same codes to save space and memory.

**style.css**

Includes the style formatting for all the elements of the page except the background photo. Although many different colors, elements and styles are used in the file, I made sure that the final design is simple and minimalistic. The main colors used are blue in different shades and purple. Some of the unique styles used are the hover for the button, the placeholder in the form and opacity of used for the form and the header background.

**application.py**

This file contains all the conditionals, arguments and the calculations that takes the user input and sends back the result. It also handles the error messages when the user does not input a number. It handles error by using "if not" function. It uses both methods: GET and POST and takes the user input in the type of "float". Once all fields are completed and the result is checked by making sure it's not smaller than 0, the results are rendered to the inedx.html file to show it on the page. Overall, the inputs from the user are grabbed by the last function named "breakEven" that applies a functional calculation to calculate the number of units the user needs to sell hypothetically to cover all their costs and reach a breakeven point given all the inputs available.