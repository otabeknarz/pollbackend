from django.db import models
from django.contrib.auth.models import AbstractUser
import random


def get_random_id() -> str:
    return str(random.randint(1000000000, 9999999999))


class User(AbstractUser):
    class PollChoices(models.TextChoices):
        MAKTAB_1 = "MAKTAB_1", "1-мактаб"
        MAKTAB_2 = "MAKTAB_2", "2-мактаб"
        MAKTAB_3 = "MAKTAB_3", "3-мактаб"
        MAKTAB_4 = "MAKTAB_4", "4-мактаб"
        MAKTAB_5_IDUM = "MAKTAB_5_IDUM", "5-ИДУМ"
        MAKTAB_6 = "MAKTAB_6", "6-мактаб"
        MAKTAB_7 = "MAKTAB_7", "7-мактаб"
        MAKTAB_8 = "MAKTAB_8", "8-мактаб"
        MAKTAB_9 = "MAKTAB_9", "9-мактаб"
        MAKTAB_10 = "MAKTAB_10", "10-мактаб"
        MAKTAB_11 = "MAKTAB_11", "11-мактаб"
        MAKTAB_12 = "MAKTAB_12", "12-мактаб"
        MAKTAB_13 = "MAKTAB_13", "13-мактаб"
        MAKTAB_14 = "MAKTAB_14", "14-мактаб"
        MAKTAB_15 = "MAKTAB_15", "15-мактаб"
        MAKTAB_16 = "MAKTAB_16", "16-мактаб"
        MAKTAB_17 = "MAKTAB_17", "17-мактаб"
        MAKTAB_18 = "MAKTAB_18", "18-мактаб"
        MAKTAB_19 = "MAKTAB_19", "19-мактаб"
        MAKTAB_20 = "MAKTAB_20", "20-мактаб"
        MAKTAB_21 = "MAKTAB_21", "21-мактаб"
        MAKTAB_22 = "MAKTAB_22", "22-мактаб"
        MAKTAB_23 = "MAKTAB_23", "23-мактаб"
        MAKTAB_24 = "MAKTAB_24", "24-мактаб"
        MAKTAB_25 = "MAKTAB_25", "25-мактаб"
        MAKTAB_26 = "MAKTAB_26", "26-мактаб"
        MAKTAB_27 = "MAKTAB_27", "27-мактаб"
        MAKTAB_28 = "MAKTAB_28", "28-мактаб"
        MAKTAB_29 = "MAKTAB_29", "29-мактаб"
        MAKTAB_30 = "MAKTAB_30", "30-мактаб"
        MAKTAB_31 = "MAKTAB_31", "31-мактаб"
        MAKTAB_32 = "MAKTAB_32", "32-мактаб"
        MAKTAB_33 = "MAKTAB_33", "33-мактаб"
        MAKTAB_34 = "MAKTAB_34", "34-мактаб"
        MAKTAB_35 = "MAKTAB_35", "35-мактаб"
        MAKTAB_36 = "MAKTAB_36", "36-мактаб"
        MAKTAB_37 = "MAKTAB_37", "37-мактаб"
        MAKTAB_38 = "MAKTAB_38", "38-мактаб"
        MAKTAB_39 = "MAKTAB_39", "39-мактаб"
        MAKTAB_40 = "MAKTAB_40", "40-мактаб"
        MAKTAB_41 = "MAKTAB_41", "41-мактаб"
        MAKTAB_42 = "MAKTAB_42", "42-мактаб"
        MAKTAB_43 = "MAKTAB_43", "43-мактаб"
        MAKTAB_44 = "MAKTAB_44", "44-мактаб"
        MAKTAB_45_IDUM = "MAKTAB_45_IDUM", "45-ИДУМ"
        MAKTAB_46 = "MAKTAB_46", "46-мактаб"
        MAKTAB_47 = "MAKTAB_47", "47-мактаб"
        MAKTAB_48 = "MAKTAB_48", "48-мактаб"
        MAKTAB_49 = "MAKTAB_49", "49-мактаб"
        MAKTAB_50 = "MAKTAB_50", "50-мактаб"
        MAKTAB_51 = "MAKTAB_51", "51-мактаб"
        MAKTAB_52 = "MAKTAB_52", "52-мактаб"
        MAKTAB_53 = "MAKTAB_53", "53-мактаб"
        MAKTAB_54 = "MAKTAB_54", "54-мактаб"
        MAKTAB_55 = "MAKTAB_55", "55-мактаб"
        MAKTAB_56 = "MAKTAB_56", "56-мактаб"
        MAKTAB_57 = "MAKTAB_57", "57-мактаб"
        MAKTAB_58 = "MAKTAB_58", "58-мактаб"
        MAKTAB_59 = "MAKTAB_59", "59-мактаб"
        MAKTAB_60_IDUM = "MAKTAB_60_IDUM", "60-ИДУМ"
        MAKTAB_61_IDUM = "MAKTAB_61_IDUM", "61-ИДУМ"
        MAKTAB_62_IDUM = "MAKTAB_62_IDUM", "62-ИДУМ"
        MAKTAB_63_IDUM = "MAKTAB_63_IDUM", "63-ИДУМ"
        MAKTAB_64 = "MAKTAB_64", "64-мактаб"
        MAKTAB_65 = "MAKTAB_65", "65-мактаб"
        MAKTAB_66 = "MAKTAB_66", "66-мактаб"
        MAKTAB_67 = "MAKTAB_67", "67-мактаб"

    id = models.CharField(
        max_length=40,
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        default=get_random_id,
    )
    email = models.EmailField(null=True, blank=True)
    choice = models.CharField(
        max_length=20, choices=PollChoices.choices, null=True, blank=True
    )

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
