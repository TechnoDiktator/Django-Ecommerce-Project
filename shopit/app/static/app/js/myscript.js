    $('#slider1, #slider2, #slider3').owlCarousel({
        loop: true,
        margin: 20,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false,
                autoplay: true,
            },
            600: {
                items: 3,
                nav: true,
                autoplay: true,
            },
            1000: {
                items: 5,
                nav: true,
                loop: true,
                autoplay: true,
            }
        }
    })


    $('.minus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        console.log(id)
        var eml = this.parentNode.children[2]
        console.log(id)
        console.log("plus clicked")
        $.ajax({
            type:"GET",
            url:"/minuscart",
            data:{
                prod_id:id
            },
            success: function(data){
                console.log(data)
                console.log("success" , data)
                eml.innerText = data.quantity
                document.getElementById("amount").innerText = data.amount
                document.getElementById("totalamount").innerText = data.totalamount
                document.getElementById("shippingamount").innerText = data.shippingamount

            }

        })

    })




    $('.plus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        console.log(id)
        var eml = this.parentNode.children[2]
        console.log(id)
        console.log("plus clicked")
        $.ajax({
            type:"GET",
            url:"/pluscart",
            data:{
                prod_id:id
            },
            success: function(data){
                console.log(data)
                console.log("success" , data)
                eml.innerText = data.quantity
                document.getElementById("amount").innerText = data.amount
                document.getElementById("totalamount").innerText = data.totalamount
                document.getElementById("shippingamount").innerText = data.shippingamount

            }

        })
    })

    $('.remove-cart').click(function(){
        var id = $(this).attr("pid").toString();
        console.log("remove clicked")
        var eml = this
        $.ajax({
            type:"GET",
            url:"/removecart",
            data:{
                prod_id:id
            },
            success: function(data){
                console.log(data)
                console.log("success" , data)
                eml.innerText = data.quantity
                document.getElementById("amount").innerText = data.amount
                document.getElementById("totalamount").innerText = data.totalamount
                document.getElementById("shippingamount").innerText = data.shippingamount
                eml.parentNode.parentNode.parentNode.parentNode.remove()
            }

        })

    })



