using backend.Application.Interfaces;
using backend.Domain.Entities;
using backend.Domain.Interfaces;

namespace backend.Application.Services
{
    public class QuotationService : IQuotationService
    {
        private readonly IQuotationRepository _quotationRepository;

        public QuotationService(IQuotationRepository quotationRepository)
        {
            _quotationRepository = quotationRepository;
        }

        public async Task<Quotation> GetQuotationAsync(string currencyFrom, string currencyTo)
        {
            return await _quotationRepository.GetQuotationAsync(currencyFrom, currencyTo);
        }
    }
}