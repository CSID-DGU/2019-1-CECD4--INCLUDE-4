(function() {
    $(function() {
      var verif_confirm, verif_empty;
      verif_empty = function(field) {
        return $('#f_' + field).keyup(function() {
          var $mess, $text;
          $mess = $('#' + field + '-field');
          if ($(this).val() !== '') {
            $(this).add($mess).addClass('valid');
            $text = $mess.text().replace("empty", "correct");
          } else {
            $(this).add($mess).removeClass('valid');
            $text = $mess.text().replace("correct", "empty");
          }
          return $mess.text($text);
        });
      };
      verif_confirm = function(field) {
        return $('#f_' + field).keyup(function() {
          var $mess, $text;
          $mess = $('#' + field + '-field');
          if ($(this).val() === $('#f_password').val()) {
            $(this).add($mess).addClass('valid');
            $text = $mess.text().replace("doesn't match", "is correct");
          } else {
            $(this).add($mess).removeClass('valid');
            $text = $mess.text().replace("is correct", "doesn't match");
          }
          return $mess.text($text);
        });
      };
      verif_empty('name');
      verif_empty('email');
      verif_empty('password');
      verif_empty('name');
      return verif_confirm('confirm');
    });
  
  }).call(this);
  
  //# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiPGFub255bW91cz4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFBQSxDQUFBLENBQUUsUUFBQSxDQUFBLENBQUE7QUFDQSxRQUFBLGFBQUEsRUFBQTtJQUFBLFdBQUEsR0FBYyxRQUFBLENBQUMsS0FBRCxDQUFBO2FBQ1osQ0FBQSxDQUFFLEtBQUEsR0FBUSxLQUFWLENBQWdCLENBQUMsS0FBakIsQ0FBdUIsUUFBQSxDQUFBLENBQUE7QUFDckIsWUFBQSxLQUFBLEVBQUE7UUFBQSxLQUFBLEdBQVEsQ0FBQSxDQUFFLEdBQUEsR0FBTSxLQUFOLEdBQWMsUUFBaEI7UUFDUixJQUFHLENBQUEsQ0FBRSxJQUFGLENBQUksQ0FBQyxHQUFMLENBQUEsQ0FBQSxLQUFnQixFQUFuQjtVQUNFLENBQUEsQ0FBRSxJQUFGLENBQUksQ0FBQyxHQUFMLENBQVMsS0FBVCxDQUFlLENBQUMsUUFBaEIsQ0FBeUIsT0FBekI7VUFDQSxLQUFBLEdBQVEsS0FBSyxDQUFDLElBQU4sQ0FBQSxDQUFZLENBQUMsT0FBYixDQUFxQixPQUFyQixFQUE4QixTQUE5QixFQUZWO1NBQUEsTUFBQTtVQUlFLENBQUEsQ0FBRSxJQUFGLENBQUksQ0FBQyxHQUFMLENBQVMsS0FBVCxDQUFlLENBQUMsV0FBaEIsQ0FBNEIsT0FBNUI7VUFDQSxLQUFBLEdBQVEsS0FBSyxDQUFDLElBQU4sQ0FBQSxDQUFZLENBQUMsT0FBYixDQUFxQixTQUFyQixFQUFnQyxPQUFoQyxFQUxWOztlQU9BLEtBQUssQ0FBQyxJQUFOLENBQVcsS0FBWDtNQVRxQixDQUF2QjtJQURZO0lBWWQsYUFBQSxHQUFnQixRQUFBLENBQUMsS0FBRCxDQUFBO2FBQ2QsQ0FBQSxDQUFFLEtBQUEsR0FBUSxLQUFWLENBQWdCLENBQUMsS0FBakIsQ0FBdUIsUUFBQSxDQUFBLENBQUE7QUFDckIsWUFBQSxLQUFBLEVBQUE7UUFBQSxLQUFBLEdBQVEsQ0FBQSxDQUFFLEdBQUEsR0FBTSxLQUFOLEdBQWMsUUFBaEI7UUFDUixJQUFHLENBQUEsQ0FBRSxJQUFGLENBQUksQ0FBQyxHQUFMLENBQUEsQ0FBQSxLQUFjLENBQUEsQ0FBRSxhQUFGLENBQWdCLENBQUMsR0FBakIsQ0FBQSxDQUFqQjtVQUNFLENBQUEsQ0FBRSxJQUFGLENBQUksQ0FBQyxHQUFMLENBQVMsS0FBVCxDQUFlLENBQUMsUUFBaEIsQ0FBeUIsT0FBekI7VUFDQSxLQUFBLEdBQVEsS0FBSyxDQUFDLElBQU4sQ0FBQSxDQUFZLENBQUMsT0FBYixDQUFxQixlQUFyQixFQUFzQyxZQUF0QyxFQUZWO1NBQUEsTUFBQTtVQUlFLENBQUEsQ0FBRSxJQUFGLENBQUksQ0FBQyxHQUFMLENBQVMsS0FBVCxDQUFlLENBQUMsV0FBaEIsQ0FBNEIsT0FBNUI7VUFDQSxLQUFBLEdBQVEsS0FBSyxDQUFDLElBQU4sQ0FBQSxDQUFZLENBQUMsT0FBYixDQUFxQixZQUFyQixFQUFtQyxlQUFuQyxFQUxWOztlQU9BLEtBQUssQ0FBQyxJQUFOLENBQVcsS0FBWDtNQVRxQixDQUF2QjtJQURjO0lBWWhCLFdBQUEsQ0FBWSxPQUFaO0lBQ0EsV0FBQSxDQUFZLE1BQVo7SUFDQSxXQUFBLENBQVksVUFBWjtXQUNBLGFBQUEsQ0FBYyxTQUFkO0VBNUJBLENBQUY7QUFBQSIsInNvdXJjZXNDb250ZW50IjpbIiQgLT5cbiAgdmVyaWZfZW1wdHkgPSAoZmllbGQpIC0+XG4gICAgJCgnI2ZfJyArIGZpZWxkKS5rZXl1cCAtPlxuICAgICAgJG1lc3MgPSAkKCcjJyArIGZpZWxkICsgJy1maWVsZCcpXG4gICAgICBpZiAkKEApLnZhbCgpIGlzbnQgJydcbiAgICAgICAgJChAKS5hZGQoJG1lc3MpLmFkZENsYXNzICd2YWxpZCdcbiAgICAgICAgJHRleHQgPSAkbWVzcy50ZXh0KCkucmVwbGFjZShcImVtcHR5XCIsIFwiY29ycmVjdFwiKVxuICAgICAgZWxzZVxuICAgICAgICAkKEApLmFkZCgkbWVzcykucmVtb3ZlQ2xhc3MgJ3ZhbGlkJ1xuICAgICAgICAkdGV4dCA9ICRtZXNzLnRleHQoKS5yZXBsYWNlKFwiY29ycmVjdFwiLCBcImVtcHR5XCIpXG5cbiAgICAgICRtZXNzLnRleHQoJHRleHQpXG5cbiAgdmVyaWZfY29uZmlybSA9IChmaWVsZCkgLT5cbiAgICAkKCcjZl8nICsgZmllbGQpLmtleXVwIC0+XG4gICAgICAkbWVzcyA9ICQoJyMnICsgZmllbGQgKyAnLWZpZWxkJylcbiAgICAgIGlmICQoQCkudmFsKCkgaXMgJCgnI2ZfcGFzc3dvcmQnKS52YWwoKVxuICAgICAgICAkKEApLmFkZCgkbWVzcykuYWRkQ2xhc3MgJ3ZhbGlkJ1xuICAgICAgICAkdGV4dCA9ICRtZXNzLnRleHQoKS5yZXBsYWNlKFwiZG9lc24ndCBtYXRjaFwiLCBcImlzIGNvcnJlY3RcIilcbiAgICAgIGVsc2VcbiAgICAgICAgJChAKS5hZGQoJG1lc3MpLnJlbW92ZUNsYXNzICd2YWxpZCdcbiAgICAgICAgJHRleHQgPSAkbWVzcy50ZXh0KCkucmVwbGFjZShcImlzIGNvcnJlY3RcIiwgXCJkb2Vzbid0IG1hdGNoXCIpXG5cbiAgICAgICRtZXNzLnRleHQoJHRleHQpXG5cbiAgdmVyaWZfZW1wdHkoJ2ZpcnN0JylcbiAgdmVyaWZfZW1wdHkoJ2xhc3QnKVxuICB2ZXJpZl9lbXB0eSgncGFzc3dvcmQnKVxuICB2ZXJpZl9jb25maXJtKCdjb25maXJtJykiXX0=
  //# sourceURL=coffeescript