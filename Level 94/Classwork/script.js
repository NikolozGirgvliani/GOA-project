const Class = {
  studentCount: 17,
  grade: 7,
  favSubject: 'English'
};

if (Class.studentCount > 30) {
  console.log('very big class');
} else {
  console.log('Small Class');
}

if (Class.grade >= 9) {
  console.log('HighSchool');
} else {
  console.log('Middle school');
}

if (Class.favSubject == 'English') {
  console.log('Loves English');
} else {
  console.log('Other favorite subject');
}
