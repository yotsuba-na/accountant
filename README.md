# homenet


#### Routes
- [ ] / - widgets, summary, navbar with data and quick links
- [ ] /auth
  - [ ] /login
  - [ ] /register
  - [ ] /reset
  - [ ] /confirm
- [ ] /finance
  - [ ] /user/<user_id>
- [ ] /crud - main crud page for all users to vote ?!
  - [ ] /user/<user_id>
- [ ] /user/<user_id>


#### Finance
```
$summary = (in+out)

  @table.left { filter_by: month, *custom* }
  --------+-----------+--------
  User_1  |  User_2   | User_N
  summary |  summary  | summary

 @table.left
          +-----------+
          |  summary  |
          +-----------+

  @table.right {pagination: On/Off, filter_by: user}
  monthly summary
    -------+---------+---------
    User_N | -139 r. | datetime


### _View_page_body

    { block navbar }
         navbar

    { block container }
    =============================================
    { block top }
        $filter.date(%Y-%m) || $summary.filtered {$currencies} || $summary {$currencies}

    { block table-left } || { block table-right }
          Table summary  ||       Table expenses
          Table users    ||
```
