# accountant

#### Routes
- [ ] /
- [ ] /auth
  - [ ] /login
  - [ ] /register
  - [ ] /reset
  - [ ] /confirm
- [ ] /finance
  - [ ] /<user_id>
- [ ] /home
- [ ] /user/<user_id>



#### Finance
```
$summary = (in+out)

  @table { filter_by: month, *custom* }
  --------+-----------+--------
  User_1  |  User_2   | User_N
  summary |  summary  | summary
 
          +-----------+
          |  summary  |
          +-----------+

  @table {pagination: On/Off, filter_by: user}
  monthly summary
    -------+---------+---------
    User_N | -139 r. | datetime
```
