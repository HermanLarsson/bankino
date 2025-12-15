# Style-guide for Project Bank

1. Windows
2. Fonts
3. Colors
4. Buttons
5. Placement

## 1. Windows
There are two kinds of windows - 
### Main Windows
### Sub Windows

**Main Windows** are 1000x1000 pixels by default and resizable. Grid layout is 10x20.
**Sub-windows** are 600x600, with a 20x20 grid. 

All windows should have the following `window_name.resizable(width=False, height=False)` in their initialization to avoid resizing.

## 2. Fonts
Main font for this program is calibri
 - **header\_font** is used for the main title for windows.
 - **header2\_font** can be used for the title of a section of a window.
 - **body\_font** is the font used for any and all other text in the window.
 - **value\_font** is used to denote monetary value.
 - **button\_font** is used for any buttons that are not navigation buttons
 - **nav\_font** is used for navigation menu buttons
Bold text can be used for other sub-sub-titles.

## 3. Colors
Main text color is #333333. A very dark gray, but _not_ black!
Background color for windows is always #F5F5F0, and _not_ full white!

## 4. Buttons
Buttons shall have the follow variables applied:
 - font = button\_font
 - bg = "#FFFFFF"
 - fg = "#333333"
 
## 5. Placement
Any titles, headers and navigation bars are placed by pixel-value while the data / text / input fields being displayed are assigned through the grid.

Every window should include the Top-bar which is a frame covering the top 200 pixels in green.
This bar is defined below.

<<nav_bar = tk.Frame(landing_page, bg = "#5D866C", width = 1000, height = 124)>>
<<nav_bar.place(x = 0, y = 0)>>

The header for the window (using header_font) should be applied at x20:y16. Any sub-titles are to be x20 and y any value that makes sense for the placement of the sub title.