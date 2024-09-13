# Generated by Django 4.2.15 on 2024-09-08 23:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("engine", "0083_job_parent_job_task_consensus_jobs_per_regular_job_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConsensusSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("agreement_score_threshold", models.FloatField(default=0)),
                ("quorum", models.IntegerField(default=-1)),
                ("iou_threshold", models.FloatField(default=0.5)),
                ("sigma", models.FloatField(default=0.1)),
                ("line_thickness", models.FloatField(default=0.01)),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consensus_settings",
                        to="engine.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConsensusReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("target_last_updated", models.DateTimeField()),
                ("consensus_score", models.IntegerField()),
                ("data", models.JSONField()),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="consensus",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consensus_reports",
                        to="engine.job",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children_reports",
                        to="consensus.consensusreport",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consensus_reports",
                        to="engine.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConsensusConflict",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("frame", models.PositiveIntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("no_matching_item", "NoMatchingItemError"),
                            ("no_matching_annotation", "NoMatchingAnnError"),
                            ("annotation_too_close", "AnnotationsTooCloseError"),
                            ("failed_label_voting", "FailedLabelVotingError"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conflicts",
                        to="consensus.consensusreport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssigneeConsensusReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("consensus_score", models.IntegerField()),
                ("conflict_count", models.IntegerField()),
                ("consensus_report_id", models.PositiveIntegerField()),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assignee_consensus_reports",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignee_consensus_reports",
                        to="engine.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnnotationId",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("obj_id", models.PositiveIntegerField()),
                ("job_id", models.PositiveIntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[("tag", "TAG"), ("shape", "SHAPE"), ("track", "TRACK")],
                        max_length=32,
                    ),
                ),
                (
                    "shape_type",
                    models.CharField(
                        choices=[
                            ("rectangle", "RECTANGLE"),
                            ("polygon", "POLYGON"),
                            ("polyline", "POLYLINE"),
                            ("points", "POINTS"),
                            ("ellipse", "ELLIPSE"),
                            ("cuboid", "CUBOID"),
                            ("mask", "MASK"),
                            ("skeleton", "SKELETON"),
                        ],
                        default=None,
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "conflict",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annotation_ids",
                        to="consensus.consensusconflict",
                    ),
                ),
            ],
        ),
    ]