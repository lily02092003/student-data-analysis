function validateForm() {
    var gender = document.forms["predictionForm"]["gender"].value;
    var ethnicity = document.forms["predictionForm"]["ethnicity"].value;
    var parentalEducation = document.forms["predictionForm"]["parental_level_of_education"].value;
    var lunch = document.forms["predictionForm"]["lunch"].value;
    var testCourse = document.forms["predictionForm"]["test_preparation_course"].value;
    var readingScore = document.forms["predictionForm"]["reading_score"].value;
    var writingScore = document.forms["predictionForm"]["writing_score"].value;

    if (gender === "") {
        alert("Please select your gender.");
        return false;
    }

    if (ethnicity === "") {
        alert("Please select your ethnicity.");
        return false;
    }

    if (parentalEducation === "") {
        alert("Please select your parental education level.");
        return false;
    }

    if (lunch === "") {
        alert("Please select your lunch type.");
        return false;
    }

    if (testCourse === "") {
        alert("Please select your test preparation course status.");
        return false;
    }

    if (readingScore === "" || isNaN(readingScore) || readingScore < 0 || readingScore > 100) {
        alert("Please enter a valid reading score between 0 and 100.");
        return false;
    }

    if (writingScore === "" || isNaN(writingScore) || writingScore < 0 || writingScore > 100) {
        alert("Please enter a valid writing score between 0 and 100.");
        return false;
    }

    return true; // Return false to prevent form submission
}
