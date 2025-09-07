# CredKit CRM - Entity-Relationship Diagram (Text-based)

This document outlines the database schema for the CredKit CRM application.

## Tables

### `accounts`
The central tenant model. Every other piece of data is associated with an account.
- `id` (PK)
- `name`
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `users`
Stores user accounts. Can be Owners, Staff, or Clients.
- `id` (PK)
- `email`
- `hashed_password`
- `is_active`
- `role` (Enum: OWNER, STAFF, CLIENT)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`
- **Unique Constraint:** (`account_id`, `email`)

### `client_profiles`
Detailed information for users with the `CLIENT` role.
- `id` (PK)
- `first_name`, `last_name`, `email`, `phone_number`, `address`, `city`, `state`, `zip_code`
- `user_id` (FK to `users.id`)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`
- **Unique Constraint:** (`account_id`, `email`)

### `leads`
Potential clients.
- `id` (PK)
- `first_name`, `last_name`, `email`, `phone_number`
- `status` (e.g., "new", "contacted", "converted")
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `credit_bureaus` (Seed Data)
The three major credit bureaus.
- `id` (PK)
- `name` (unique)
- `website`
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `creditors` (Seed Data)
Financial institutions or other entities that report to credit bureaus.
- `id` (PK)
- `name` (unique)
- `address`
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `dispute_cases`
A container for a client's dispute items.
- `id` (PK)
- `status` (e.g., "open", "closed")
- `client_id` (FK to `client_profiles.id`)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `dispute_items`
A specific item being disputed.
- `id` (PK)
- `item_type` (e.g., "tradeline", "collection", "public_record")
- `status` (e.g., "pending", "disputed", "resolved")
- `reason` (text)
- `case_id` (FK to `dispute_cases.id`)
- `bureau_id` (FK to `credit_bureaus.id`)
- `creditor_id` (FK to `creditors.id`, nullable)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `letter_templates`
Reusable templates for dispute letters.
- `id` (PK)
- `name`, `subject`, `body` (text)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `generated_letters`
A record of a letter that has been generated from a template.
- `id` (PK)
- `content` (text)
- `case_id` (FK to `dispute_cases.id`)
- `template_id` (FK to `letter_templates.id`)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `tasks`
Tasks for staff members.
- `id` (PK)
- `title`, `description` (text), `due_date`, `status`
- `assigned_to_id` (FK to `users.id`, nullable)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `notes`
Polymorphic notes that can be attached to various records.
- `id` (PK)
- `content` (text)
- `author_id` (FK to `users.id`)
- `parent_id` (Integer, the ID of the parent record)
- `parent_type` (String, the type of the parent record, e.g., "ClientProfile")
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `attachments`
Polymorphic attachments.
- `id` (PK)
- `file_name`, `file_path`, `file_type`
- `parent_id`
- `parent_type`
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `invoices`
Invoices for client billing.
- `id` (PK)
- `amount`, `due_date`, `status`
- `client_id` (FK to `client_profiles.id`)
- `subscription_id` (FK to `subscriptions.id`, nullable)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `subscriptions`
Client subscriptions (e.g., via Stripe).
- `id` (PK)
- `stripe_subscription_id` (unique)
- `status`, `plan`, `price`, `current_period_end`
- `client_id` (FK to `client_profiles.id`)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `webhook_events`
Stores incoming webhook events for later processing.
- `id` (PK)
- `source` (e.g., "stripe"), `event_type`
- `payload` (JSON)
- `status`, `error_message` (text)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`

### `audit_logs`
Tracks important events in the system.
- `id` (PK)
- `action`, `details` (text), `changes` (JSON)
- `user_id` (FK to `users.id`, nullable)
- `target_id`, `target_type` (polymorphic)
- `account_id` (FK to `accounts.id`)
- `created_at`, `updated_at`, `deleted_at`
- `version`
