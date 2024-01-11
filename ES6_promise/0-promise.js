function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const condition = true; 
    if (condition) {
      resolve();
    } else {
      reject();
    }
  });
}

export default getResponseFromAPI;
