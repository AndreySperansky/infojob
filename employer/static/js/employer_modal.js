console.log("Hello from Employer modals!")

$(function () {
          // Log in & Sign up buttons
          // The formURL is given explicitly
          $("#login-btn").modalForm({
            formURL: "{% url 'login' %}"
          });

          $("#signup-btn").modalForm({
            formURL: "{% url 'signup' %}"
          });

          

          // Read and Delete bookmark buttons open modal with id="modal"
          // The formURL is retrieved from the data of the element
          $(".read-bookmark").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url")});
              console.log("Hello from read!")
          });

  
          $(".response").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url")});
          });
          
          
          $(".delete-bookmark").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
          });
          
          
          $(".delete-response").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
          });
          
           // Filter button
          $("#filter").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url")});
          });

          // Hide message
  
          // $(".alert").fadeTo(2000, 500).slideUp(500, function () {
          //     $(".alert").slideUp(500);
          // });
      });