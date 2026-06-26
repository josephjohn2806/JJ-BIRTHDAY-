using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace BirthdaySite.Controllers
{
    [ApiController]
    [Route("api")]
    public class BirthdayController : ControllerBase
    {
        private static readonly List<WishModel> Wishes = new()
        {
            new WishModel { Name = "Peter", Text = "Happy Birthday JJ! Let's conquer more milestones." }
        };

        [HttpGet("wishes")]
        public IActionResult GetWishes() => Ok(Wishes);

        [HttpPost("wishes")]
        public IActionResult AddWish([FromBody] WishModel newWish)
        {
            Wishes.Insert(0, newWish);
            return StatusCode(201, new { status = "Success" });
        }

        [HttpPost("gift/mpesa")]
        public IActionResult ProcessMpesaGift([FromBody] MpesaRequest request)
        {
            // Logging values to terminal context
            System.Diagnostics.Debug.WriteLine($"Processing Mpesa execution for {request.Phone} - KES {request.Amount}");
            return Ok(new { Status = "STK Push Dispatched", CheckoutRequestID = "cs_CO_9983421" });
        }
    }

    public class WishModel 
    { 
        public string Name { get; set; } 
        public string Text { get; set; } 
    }

    public class MpesaRequest 
    { 
        public string Phone { get; set; } 
        public decimal Amount { get; set; } 
    }
}
