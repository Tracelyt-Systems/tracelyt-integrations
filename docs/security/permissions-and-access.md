# Permissions and Access Control

This document defines the principle of least privilege, operating system access boundaries, and database permission standards for **Tracelyt Integrations**.

---

## 1. Principle of Least Privilege

Integrations must always run with the minimal permissions required to capture telemetry:
- **Never Run as Root / Administrator**: Containerized OpenTelemetry collectors and monitored applications should execute as unprivileged, dedicated non-root service accounts (`UID 10001` or `otelcol`).
- **Read-Only Defaults**: Telemetry collectors require read access to specific logs, metrics endpoints, or system `/proc` counters. Write permissions to application databases, message queues, or host filesystems are strictly prohibited.

---

## 2. Infrastructure & Host Monitoring Privileges

When collecting host or container metrics:
- **Linux `/proc` and `/sys`**: Use standard read-only mounts.
- **Docker Daemon Access**: Mount the Docker socket (`/var/run/docker.sock`) as read-only, or prefer rootless container metrics via cgroups v2.
- **Kubernetes Node Access**: The collector DaemonSet should use a restricted Kubernetes `ClusterRole` granting only `get`, `list`, and `watch` permissions on `nodes`, `namespaces`, `pods`, and `services`. It must not possess cluster administration, secret viewing, or pod mutation permissions.

---

## 3. Database Monitoring Accounts

Database integrations (e.g., MySQL, PostgreSQL, MongoDB, Redis) must never connect using superuser (`root`, `postgres`) credentials. Dedicated monitoring accounts must be provisioned with strictly scoped read-only roles:

```sql
-- Example: Least-Privilege MySQL Monitoring User
CREATE USER 'tracelyt_monitor'@'%' IDENTIFIED BY '${TRACELYT_DB_PASSWORD}';
GRANT PROCESS, REPLICATION CLIENT ON *.* TO 'tracelyt_monitor'@'%';
-- Do not grant SELECT, INSERT, UPDATE, DELETE, or DROP privileges
```

---

## 4. Related Documentation

- [Integration Threat Model](integration-threat-model.md)
- [Credential Handling](credential-handling.md)
- [Network Security](network-security.md)

