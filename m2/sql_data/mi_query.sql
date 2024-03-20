select t.title as tit,
	   year(max(pubdate)) as 'year',
       count(t.title_id) as numauthors,
       group_concat(concat(a.au_fname, ' ', a.au_lname)) as allauthors,
       avg(price) as price_avg
from titles as t
left join titleauthor as ta
on t.title_id = ta.title_id
left join authors as a
on a.au_id = ta.au_id
group by t.title
order by price_avg desc
;

/*

comentario multilinea

*/