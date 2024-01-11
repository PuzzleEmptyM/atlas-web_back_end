import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUser = signUpUser(firstName, lastName).then((response) => (
    { status: 'fulfilled', value: response }
  ));

  const failedPhoto = uploadPhoto(fileName).catch((error) => (
    { status: 'rejected', value: `Error: ${error.message}` }
  ));
  return Promise.all([signUser, failedPhoto]);
}
