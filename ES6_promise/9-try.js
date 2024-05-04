export default function guardrail(mathFunction) {
  const queue = [];
  let tryMathFunc;

  try {
    tryMathFunc = mathFunction();
  } catch (error) {
    tryMathFunc = `${error.name}: ${error.message}`;
  }

  queue.push(tryMathFunc);
  queue.push('Guardrail was processed');
  return queue;
}
