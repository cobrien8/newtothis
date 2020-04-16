/*think of a way to use variable names like player_to_search = user.input('What player would you like data on?')*/

use bball

select bbmaster.playerID,bbmaster.lastname, bbmaster.firstname, bbmaster.birthstate, batting.yearid, batting.homeruns
from bbmaster join batting
order by batting.homeruns desc;
	on bbmaster.playerID = batting.playerID where birthstate like '%AZ'
