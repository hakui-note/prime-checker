// 現時点では特にJavaScriptは必要ありませんが、必要に応じてここに記述します。
document.addEventListener('DOMContentLoaded', function() {
  const numberInput = document.getElementById('number');
  const keys = document.querySelectorAll('.key');

  keys.forEach(key => {
      key.addEventListener('click', function() {
          const value = this.getAttribute('data-value');
          if (value) {
              numberInput.value += value;
          } else if (this.classList.contains('clear')) {
              numberInput.value = '';
          }
      });
  });
  //console.log('素数判定アプリがロードされました。');
});
