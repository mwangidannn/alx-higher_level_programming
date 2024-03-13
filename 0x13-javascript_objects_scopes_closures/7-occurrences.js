#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let h = 0; h < list.length; h++) {
    count = (list[h] === searchElement ? count + 1 : count);
  }

  return count;
};
