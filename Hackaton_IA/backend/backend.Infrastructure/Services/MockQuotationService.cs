using backend.Application.Interfaces;
using backend.Domain.Entities;

namespace backend.Infrastructure.Services
{
    public class MockQuotationService : IQuotationService
    {
        public Task<Quotation> GetQuotationAsync(string currencyFrom, string currencyTo)
        {
            // Return mock data with random rate
            var random = new Random();
            var rate = (decimal)(random.NextDouble() * (6.0 - 4.0) + 4.0); // Random rate between 4.0 and 6.0

            var quotation = new Quotation
            {
                CurrencyFrom = currencyFrom,
                CurrencyTo = currencyTo,
                Rate = Math.Round(rate, 2),
                Date = DateTime.Now
            };
            return Task.FromResult(quotation);
        }
    }
}