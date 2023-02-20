-- Q1 - We want to see what is the name of the patron who took the most loans. Join the loan tables on “PatronID” with the appropriate table.
-- SELECT * from Loans INNER Join Patrons On Loans.PatronID = Patrons.PatronID; 




-- Q2 - Which Patron took the most loans.
-- SELECT Loans.PatronID, count(Loans.PatronID) from Loans INNER Join Patrons On Loans.PatronID = Patrons.PatronID GROUP BY Loans.PatronID ORDER BY count(Loans.PatronID) DESC; 



-- Q3 - Which book had the most loans against it.
-- SELECT Loans.BookID, count(Loans.BookID) from Loans INNER Join Books On Loans.BookID = Books.BookID GROUP BY Loans.BookID ORDER BY count(Loans.BookID) DESC; 



-- Q4 - Show which entry was returned late compared to the Due date
