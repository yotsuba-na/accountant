# accountant


#### Routes
- [ ] / - widgets, summary, navbar with data and quick links
- [ ] /auth
  - [ ] /login
  - [ ] /register
  - [ ] /reset
  - [ ] /confirm
- [ ] /finance
  - [ ] /<user_id>
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
```
