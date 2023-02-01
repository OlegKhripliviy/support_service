# Support service application


## Adjust the application

### Install deps

```bash
pipenv sync --dev

# Activate the environment
pipenv shell
```

# Database

```mermaid
erDiagram
    Users {
        ind id
        string fierst_name
        string last_name
        string email
        string password
        bool is_staff
        bool is_acrive
        datetime created_at
        datetime updatet_at
    }
    Tickets {
        int id
        int customer_id
        int manager_id
        string header
        text body
        datetime created_at
        datetime updatet_at
    }
    Comments {
        int id
        int prev_comment_id
        int user_id
        int ticket_id
        text body
        datetime created_at
        datetime updatet_at
    
    Users ||--o{ Tickets : ""
    Tickets ||--o{ Comments : ""
    Comments ||--o{ Comments : ""
```
